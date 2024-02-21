<script setup>
import { computed } from "vue";
import { useRouter } from "vue-router";
const router = useRouter();

import useSelectedGame from "@/use/useSelectedGame";
const { setSelectedGame } = useSelectedGame();

import { getRouterUrls } from "@/use/useGamesNames";

const routerUrls = getRouterUrls();

const props = defineProps({
  title: String,
  alias: String,
  url: String,
  imgName: String,
});

const gameStyle = computed(
  () =>
    `background-image: url(http://127.0.0.1:8080/static/game_icons/${props.imgName}`
);

const isRouterPath = computed(() => {
  const path = props.url.split("/");
  const cond = path.at(-1) in routerUrls;
  return cond;
});

function onClick(name) {
  setSelectedGame(name);
  router.push({ path: `/queue/${name}` });
}
</script>

<template>
  <button
    v-if="isRouterPath"
    @click="onClick(props.alias)"
    class="game"
    :id="props.alias"
    :style="gameStyle">
    <span>{{ props.title }}</span>
  </button>

  <a v-else class="game" :id="props.alias" :href="props.url" :style="gameStyle">
    <span>{{ props.title }}</span>
  </a>
</template>

<style lang="scss" scoped>
@import "@/assets/scss/variables";
.game {
  display: flex;
  justify-content: center;
  align-items: center;

  max-width: 400px;
  width: 100%;
  min-width: 200px;
  height: 100px;
  border-radius: 10px;
  box-shadow: none;

  transform: scale(1);
  transition: transform 0.3s linear;
  background-size: cover;
  background-repeat: no-repeat;
  background-color: $gray;

  &:focus {
    transform: scale(1.1);
  }

  & > span {
    display: inline-block;
    padding: 5px 20px;
    @extend %text-16;
    background-color: #fff;
    border-radius: 10px;
    color: #000;
  }
}

@media (hover: hover) {
  .game:hover {
    outline: 2px solid $dark;
    transform: scale(1);
    cursor: pointer;
  }
}
</style>
