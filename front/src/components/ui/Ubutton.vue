<script setup>
const props = defineProps({
  buttonType: {
    type: String,
    required: true,
    validator: (type) => type === "first" || type === "second",
  },
  href: {
    type: String,
    default: "",
  },
});
</script>

<template>
  <a
    v-if="props.href"
    :href="props.href"
    class="button"
    :class="`button_${buttonType}`">
    <span>
      <slot />
    </span>
  </a>

  <button v-else class="button" :class="`button_${buttonType}`">
    <span>
      <slot />
    </span>
  </button>
</template>

<style lang="scss" scoped>
@import "@/assets/scss/_variables.scss";

// button имеет ничего
// span - это и есть кнопка
.button {
  display: inline-block;
  position: relative;
  background-color: transparent;

  &::after {
    content: "";
    display: block;
    width: 100%;
    height: 0;

    position: absolute;
    inset: 0;
    z-index: 1;
    transition: all 1s ease-in-out;
  }

  & > span {
    display: block;
    position: relative;
    z-index: 3;
    padding: 8px 16px;
    @extend %text-16;
    font-weight: 500;
  }

  &_first > span {
    color: $primary;
    border: 1px solid $primary;
    background-color: transparent;
    transition: color 1s ease-in-out;
  }

  &_second > span {
    color: #fff;
    border: 1px solid $primary;
    background-color: $primary;
    transition: border-color 0.3s ease-in-out;
    transition: all 1s ease-in-out;
  }

  @media (hover: hover) {
    & {
      &:hover::after {
        height: 100%;
      }

      &_first:hover {
        &::after {
          background-color: $primary;
        }
        & > span {
          color: #fff;
        }
      }

      &_second:hover {
        &::after {
          background-color: #fff;
        }
        & > span {
          border-color: #fff;
          background-color: transparent;
          color: $primary;
        }
      }
    }
  }
}

@media (width <= 568px) {
  .button > span {
    padding: 6px 12px;
  }
}
</style>
