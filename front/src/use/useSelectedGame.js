import {ref} from 'vue';

const selectedGame = ref('')

export default function useSelectedGame(){
  const setSelectedGame = (name) => selectedGame.value = name;

  return {selectedGame, setSelectedGame}
}