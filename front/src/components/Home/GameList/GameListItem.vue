<script setup>
import { computed } from "vue";

import useSelectedGame from "@/use/useSelectedGame";

const { setSelectedGame } = useSelectedGame();

const routerUrls = {
  chess: "chess",
};

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

const routerUrl = computed(() => {
  const link = props.url;
  const to = new URL(link);
  return to.pathname;
});

const isRouterPath = computed(() => {
  const path = props.url.split("/");
  const cond = path.at(-1) in routerUrls;
  return cond;
});

function onClick(name) {
  setSelectedGame(name);
}
</script>

<template>
  <RouterLink
    v-if="isRouterPath"
    @click="onClick(props.alias)"
    class="game"
    :to="routerUrl"
    :id="props.alias"
    :style="gameStyle">
    <span>{{ props.title }}</span>
  </RouterLink>

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
