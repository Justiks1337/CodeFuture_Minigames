<script>
import { ref } from "vue";
import axios from 'axios';


export default {
  data() {
    return {
      response: [],
      selectedGame: ref(null),
      activeGame: ref(null),
    }
  },
  mounted() {
    axios.get('http://127.0.0.1:8080/api/v1/gameslist/')
        .then(response => {this.response = response.data})
  },
  methods: {
   onClick(url){
     console.log(url);
     window.location.href = url;
   }
  }
}

</script>

<template>
  <section class="gamelist">
    <div class="gamelist__container g-container">
      <button
        v-for="game in response"
        @click="onClick(game.url)"
        class="gamelist__game"
        :id="`${game.alias}`"
        :class="{
          'gamelist__game_selected': selectedGame === game.name,
          'gamelist__game_active': activeGame === game.name,
        }"
        :style="{'background-image': 'url(http://127.0.0.1:8080/static/game_icons/' + game.icon}">
        <div style="background: white; opacity: 0.7; position: relative; left: 30%; width: 40%; border-radius: 5px">
          <span style="color: black; font-size: 3vh">{{game.name}}</span>
        </div>
      </button>
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
   /* min-width: 200px; */
    height: 100px;
    border-radius: 10px;
    box-shadow: none;
    color: $blue;
    transform: scale(1);
    transition: transform 0.3s linear;
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
