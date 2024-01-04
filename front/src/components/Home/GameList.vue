<script setup>
import { ref } from "vue";

const gameList = ref([
  {
    title: "Игра 1",
  },
  {
    title: "Игра 2",
  },
  {
    title: "Игра 3",
  },
  {
    title: "Игра 4",
  },
]);

const selectedGame = ref(null);
const activeGame = ref(null);

function changeGame(id) {
  console.log(`You picked game with ${id} id`);

  selectedGame.value = id;
  activeGame.value = id;

  const timeout = setTimeout(() => {
    activeGame.value = null;
    clearTimeout(timeout);
  }, 1000);
  //fetch
}
</script>

<template>
  <section class="gamelist">
    <div class="gamelist__container g-container">
      <button
        @click="changeGame(game.title)"
        v-for="game in gameList"
        class="gamelist__game"
        :disabled="activeGame === game.title"
        :class="{
          'gamelist__game_selected': selectedGame === game.title,
          'gamelist__game_active': activeGame === game.title,
        }" />
    </div>
  </section>
</template>

<style lang="scss" scoped>
@import "@/assets/scss/_variables.scss";
.gamelist {
  user-select: none;
  width: 100%;
  background-color: $gamelist-fill;
  &__container {
    display: flex;
    flex-flow: column nowrap;
    justify-content: center;
    align-items: center;
    gap: 20px;
  }

  &__game {
    display: block;
    max-width: 400px;
    width: 100%;
    min-width: 200px;
    height: 50px;
    border-radius: 10px;
    box-shadow: none;
    color: $blue;
    transform: scale(1);
    transition: transform 0.3s linear;
    background-image: url("@/assets/img/test-avatar.jpeg");
    background-size: cover;
    background-repeat: no-repeat;
    background-color: $gray;

    &:focus {
      transform: scale(1.1);
    }

    &_active {
      animation: button-active 1s linear;
      outline: none !important;
    }
  }

  @media (hover: hover) {
    .gamelist__game:hover {
      outline: 2px solid $dark;
      transform: scale(1);
    }
  }
}
</style>
