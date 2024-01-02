<script setup>
import { ref } from "vue";
const amount = ref(1);
const allAmount = ref(3);
</script>

<template>
  <section class="loading-page">
    <div class="loading-page__container g-container">
      <img src="@/assets/svg/walking-man.svg" class="loading-page__img" />
      <h2 class="loading-page__title">
        Looking for your contenders <span>.</span> <span>.</span> <span>.</span>
      </h2>
      <p class="loading-page__amount">{{ amount }}/{{ allAmount }}</p>
    </div>
  </section>
</template>

<style lang="scss" scoped>
@import "@/assets/scss/_variables.scss";

.loading-page {
  background-color: $dark;
  overflow-x: hidden;
  &__img {
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
</style>
