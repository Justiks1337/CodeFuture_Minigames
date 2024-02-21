<script setup>
import { reactive } from "vue";

import { router } from "@/router/index";

import useSelectedGame from "@/use/useSelectedGame";

const { selectedGame, setSelectedGame } = useSelectedGame();

const gameState = reactive({
  connected: 0,
  all: 0,
});

function startGame(url) {
  if (url) window.location = url;

  gameState.connected = gameState.all;
  socket.close();
}

// generate userID
const userId = Date.now() + Math.ceil(Math.random() * 10000);
// generate websocket url
const url = `ws${import.meta.env.VITE_SSL}://${
  import.meta.env.VITE_HOSTNAME
}/websockets/queue/${selectedGame.value}/?user_id=${userId}`;

const socket = new WebSocket(url);

socket.onopen = (event) => {
  socket.send(userId);
};

socket.onmessage = (event) => {
  const msg = JSON.parse(event.data);
  switch (msg.type) {
    case "user.count":
      gameState.connected = msg.count;
      gameState.all = msg["max_size"];
      break;
    case "start_game_event":
      startGame(msg["url"]);
      break;
  }
};

socket.onerror = (event) => {
  if (event.code === 404) router.push({ name: "error-page" });
};
</script>

<template>
  <section class="loading-page">
    <div class="loading-page__container g-container">
      <img src="@/assets/svg/walking-man-icon.svg" />
      <h2 class="loading-page__title">
        Ищем ваших соперников <span>.</span> <span>.</span> <span>.</span>
      </h2>
      <p class="loading-page__amount">
        {{ gameState.connected }}/{{ gameState.all }}
      </p>
    </div>
  </section>
</template>

<style lang="scss" scoped>
@import "@/assets/scss/_variables.scss";

.loading-page {
  background-color: $dark;
  overflow-x: hidden;
  img {
    display: block;
    margin: 0 auto;
    max-width: 400px;
    width: 100%;
    min-width: 230px;
  }

  &__title {
    text-align: center;
    color: #fff;
    @extend %text-32;

    & > span {
      display: inline-block;

      &:first-child {
        animation: show-dot-1 3s ease-out infinite;
      }

      &:nth-of-type(2) {
        animation: show-dot-2 3s ease-out infinite;
      }

      &:last-child {
        animation: show-dot-3 3s ease-out infinite;
      }
    }
  }

  &__amount {
    text-align: center;
    color: #fff;
    @extend %text-20;
  }
}

@media (width <= 992px) {
  img {
    max-width: 300px;
    height: 330px;
  }
  .loading-page__title {
    font-size: 20px;
    line-height: 30px;
    font-weight: 500;
  }

  .loading-page__amount {
    font-size: 16px;
    line-height: 24px;
    font-weight: 400;
  }
}

@media (width <= 568px) {
  .loading-page__title {
    font-size: 16px;
    line-height: 24px;
    font-weight: 500;
  }
}

@media (height <= 720px) {
  img {
    max-width: 300px;
    height: 330px;
  }
}

@media (height <= 488px) {
  img {
    max-width: 200px;
    min-width: 200px;
    width: 200px;
    height: 230px;
  }
}

@media (height <= 374px) {
  img {
    height: 190px;
  }
}
</style>
