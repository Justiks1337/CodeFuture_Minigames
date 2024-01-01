<script setup>
import { ref } from "vue";
import Ubutton from "@/components/ui/Ubutton.vue";
import Umenu from "@/components/ui/Umenu.vue";
import UcircleImg from "@/components/ui/UcircleImg.vue";

const isOpen = ref(false);
const isLogin = ref(false);
</script>
<template>
  <header class="header">
    <div class="header__container g-container">
      <img
        src="@/assets/svg/1c-logo.svg"
        alt="1С УЧЕБНЫЙ ЦЕНТР"
        class="header__logo" />
      <nav class="header__nav">
        <ul>
          <li class="header__nav-item">
            <a href="#">Find a store</a>
          </li>

          <li class="header__nav-item">
            <a href="#">Help</a>
          </li>

          <li class="header__nav-item">
            <a href="#">John us</a>
          </li>
        </ul>
      </nav>

      <UcircleImg
        imgSrc="/src/assets/img/test-avatar.jpeg"
        class="avatar"
        v-if="isLogin" />

      <Ubutton
        v-if="!isLogin"
        buttonType="first"
        class="header__button header__button_sign-up">
        sign up
      </Ubutton>

      <Ubutton
        v-if="!isLogin"
        buttonType="second"
        class="header__button header__button_login">
        login
      </Ubutton>

      <button @click="isOpen = !isOpen" class="nav-button">
        <img src="@/assets/svg/nav-button-icon.svg" alt="меню" />
      </button>

      <Umenu class="nav-mobile" :isOpen="isOpen" :isLogin="isLogin" />
    </div>
  </header>
</template>

<style lang="scss" scoped>
@import "@/assets/scss/_variables.scss";
@import "@/assets/scss/_mixins.scss";

.header {
  position: relative;
  background-color: $dark-gray;

  &__container {
    display: flex;
    flex-flow: row nowrap;
    align-items: center;
    gap: 15px;

    .avatar {
      flex: 0 0 40px;
      margin-left: 9px; // container gap = 15px
    }
  }

  &__nav {
    display: none;
    &-item {
      display: inline-block;

      &:not(:first-child) {
        margin-left: 24px;
      }

      & > a {
        color: $light-gray;
        @include link($light-gray);
        @extend %text-16;
      }
    }
  }

  &__button {
    display: none;
    margin-left: 1px; //container gap 15px

    text-transform: uppercase;

    &:first-child {
      margin-left: 9px; //container gap 15px
    }
  }
}

.nav-mobile {
  display: block;

  position: absolute;
  z-index: 2;
  top: 40px + 32px; // nav-button height + padding-top + padding-bottom header
  left: 0;
}

.nav-button {
  width: 40px;
  height: 40px;

  display: flex;
  justify-content: center;
  align-items: center;

  background-color: transparent;
  margin-left: auto;
}

@media (hover: hover) {
  .header {
    position: static;
    &__button {
      display: block;
    }
    &__nav {
      display: block;
    }
  }
  .nav-mobile {
    display: none;
  }
  .nav-button {
    display: none;
  }
}

@media (width <= 992px) {
}

@media (width <= 568px) {
}

@media (width <= 376px) {
  .header {
    &__container {
      gap: 8px;
    }
    &__logo {
      width: 170px;
    }
  }

  .nav-button {
    width: 24px;
    height: 30px;
  }
}
</style>
