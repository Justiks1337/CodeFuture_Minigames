<script setup>
import Ubutton from "@/components/ui/Ubutton.vue";

const props = defineProps({
  isOpen: {
    type: Boolean,
    required: true,
  },
  isLogin: {
    type: Boolean,
    required: true,
  },
});
</script>

<template>
  <Transition name="mobile-menu">
    <section v-if="props.isOpen" class="menu">
      <div class="menu__container g-container">
        <nav class="menu__nav">
          <ul>
            <li class="menu__item"><a href="#">Find a store</a></li>
            <li class="menu__item"><a href="#">Help</a></li>
            <li class="menu__item"><a href="#">John us</a></li>
          </ul>
        </nav>
        <Ubutton
          v-if="!isLogin"
          buttonType="first"
          class="menu__button menu__button_sign-up">
          sign up
        </Ubutton>

        <Ubutton
          v-if="!isLogin"
          buttonType="second"
          class="menu__button menu__button_login">
          login
        </Ubutton>
      </div>
    </section>
  </Transition>
</template>

<style lang="scss" scoped>
@import "@/assets/scss/_variables.scss";
.menu {
  width: 100%;
  background-color: $dark-gray;

  &__item {
    padding: 8px;
    &:not(:first-child) {
      margin-top: 8px;
    }
    & > a {
      color: $light-gray;
      @extend %text-16;
    }
  }

  &__button {
    display: inline-block;
    margin-top: 24px;

    text-transform: uppercase;

    &:last-child {
      margin-left: 16px;
    }
  }
}

@media (width <= 992px) {
  .menu__container {
    padding-top: 24px;
  }
}
</style>
