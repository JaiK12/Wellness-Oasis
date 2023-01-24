import { ref, computed } from "vue";
import { defineStore } from "pinia";
import { useStorage } from "@vueuse/core";

export const useSigned = defineStore("counter", () => {
  const signedIn = useStorage("signedIn", ref(false));
  const userName = useStorage("userName", ref(""));
  const rowNumber = useStorage("rowNumber", ref(0));

  return { signedIn, userName, rowNumber };
});
