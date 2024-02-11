<script setup>
import { ref } from "vue";
import GameListItem from "./GameListItem.vue";

const gamelist = ref([
  // {
  //   name: "Майнкрафт",
  //   alias: "chess",
  //   url: "http://localhost:5173/queue/chess",
  //   icon: "minecraft.jpg",
  // },
]);

async function getGameList() {
  const response = await fetch("http://127.0.0.1:8080/api/v1/gameslist/", {
    method: "GET",
    mode: "no-cors",
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
