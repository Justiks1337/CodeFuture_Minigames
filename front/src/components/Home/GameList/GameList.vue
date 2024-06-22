<script setup>
import GameListItem from "@/components/Home/GameList/GameListItem.vue";

import { ref } from "vue";

const gamelist = ref([]);

async function getGameList() {
  const response = await fetch("http://127.0.0.1/api/v1/gameslist/", {
    headers: {
      "Content-type": "applicarion/json",
    },
    method: "GET",
  });

  gamelist.value = await response.json();
}

getGameList();
</script>

<template>
  <section class="gamelist">
    <div class="gamelist__container g-container">
      <GameListItem
        v-for="game in gamelist"
        :title="game.name"
        :alias="game.alias"
        :url="game.url"
        :imgName="game.icon"
        class="gamelist__game" />
    </div>
  </section>
</template>

<style lang="scss" scoped>
@import "@/assets/scss/variables";
.gamelist {
  user-select: none;
  width: 100%;
  background-color: $gamelist-fill;
  height: 100%;

  &__container {
    display: flex;
    flex-flow: column nowrap;
    justify-content: center;
    align-items: center;
    gap: 20px;
  }
}
</style>
