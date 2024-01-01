<script setup>
const props = defineProps({
  imgSrc: {
    type: String,
    default: "",
  },
});
</script>

<template>
  <span class="circle-image">
    <img :src="props.imgSrc" />
  </span>
</template>

<style lang="scss" scoped>
.circle-image {
  display: inline-block;
  border-radius: 50%;
  overflow: hidden;
  width: 40px;
  height: 40px;
  background-color: transparent;
}
.circle-image > img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
