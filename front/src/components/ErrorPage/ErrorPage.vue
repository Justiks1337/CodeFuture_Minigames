<script setup>
import Ubutton from "@/components/ui/Ubutton.vue";
</script>

<template>
  <section class="error-page">
    <div class="error-page__container g-container">
      <h2 class="error-page__title">404 error</h2>
      <h3 class="error-page__subtitle">
        Whoops!<br />
        Something<br />
        went wrong
      </h3>
      <p class="error-page__reason">
        Sorry, the page are looking for doesn’t exist or has been removed. Try
        searching our site.
      </p>
      <div class="error-page__buttons">
        <Ubutton href="#" buttonType="first" class="error-page__button">
          <svg
            width="7.410034"
            height="12.000000"
            viewBox="0 0 7.41003 12"
            fill="none"
            xmlns="http://www.w3.org/2000/svg"
            xmlns:xlink="http://www.w3.org/1999/xlink">
            <defs />
            <path
              id="Vector"
              d="M7.41003 10.59L2.82996 6L7.41003 1.41L6 0L0 6L6 12L7.41003 10.59Z"
              fill-rule="nonzero"
              fill="#FF1F44" />
          </svg>
          go back
        </Ubutton>

        <Ubutton href="#" buttonType="second" class="error-page__button">
          go to the main page
        </Ubutton>
      </div>
    </div>
  </section>
</template>

<style lang="scss" scoped>
@import "@/assets/scss/_variables.scss";
.error-page {
  background-color: rgb(18, 18, 18);

  &__container {
    max-width: 450px + 88px + 88px;
    margin-left: 0;

    & > *:not(:first-child) {
      margin-top: 30px;
    }
  }

  &__title {
    color: #fff;
    letter-spacing: -2.5px;
    @extend %text-32;
  }

  &__subtitle {
    color: $primary;
    @extend %text-60;
  }

  &__reason {
    color: rgba(164, 164, 164, 1);
    @extend %text-16;
  }

  &__button {
    text-transform: uppercase;

    &:not(:first-child) {
      margin-left: 30px;
    }
  }
}

@media (hover: hover) {
  svg path {
    transition: fill 1s ease-in-out; // time = time of height of after element in Ubutton component
  }

  .error-page__button:first-child:hover svg path {
    fill: #fff;
  }
}

@media (width<=992px) {
  .error-page__container {
    max-width: 450px + 64px;
  }
}

@media (width<=568px) {
  .error-page__container {
    max-width: 280px;
  }
  .error-page__button {
    display: block;
    &:not(:first-child) {
      margin-left: 0;
      margin-top: 15px;
    }
  }
}

@media (height <= 542px) {
  .error-page__title {
    font-size: 20px;
    line-height: 30px;
  }

  .error-page__subtitle {
    font-size: 32px;
    line-height: 40px;
  }
  .error-page__container > *:not(:first-child) {
    margin-top: 15px;
  }
}
</style>
