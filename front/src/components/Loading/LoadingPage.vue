<script setup>
import { ref } from "vue";
const amount = ref(1);
const allAmount = ref(3);
</script>

<template>
  <section class="loading-page">
    <div class="loading-page__container g-container">
      <img src="@/assets/svg/walking-man-icon.svg" />
      <h2 class="loading-page__title">
        Ищем ваших соперников <span>.</span> <span>.</span> <span>.</span>
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
