"use strict";(self.webpackChunk_JUPYTERLAB_CORE_OUTPUT=self.webpackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[1440],{61440:(e,t,a)=>{a.r(t),a.d(t,{CommandIDs:()=>n,default:()=>g});var n,o=a(12867),s=a(47343),l=a(55101),i=a(53979),r=a(61345);!function(e){e.installAdditionalLanguages="jupyterlab-translation:install-additional-languages"}(n||(n={}));const c="@jupyterlab/translation-extension:plugin",u={id:"@jupyterlab/translation:translator",autoStart:!0,requires:[o.JupyterFrontEnd.IPaths,i.ISettingRegistry],provides:r.ITranslator,activate:async(e,t,a)=>{const n=await a.load(c),o=n.get("locale").composite;let s=n.get("stringsPrefix").composite;s=n.get("displayStringsPrefix").composite?s:"";const l=e.serviceManager.serverSettings,i=new r.TranslationManager(t.urls.translations,s,l);return await i.fetch(o),i}},d={id:c,requires:[l.IMainMenu,i.ISettingRegistry,r.ITranslator],autoStart:!0,activate:(e,t,a,n)=>{const o=n.load("jupyterlab"),{commands:l}=e;let i;function u(e){i=e.get("locale").composite}a.load(c).then((a=>{var n;u(a),document.documentElement.lang=i,a.changed.connect(u);const c=null===(n=t.settingsMenu.items.find((e=>{var t;return"submenu"===e.type&&"jp-mainmenu-settings-language"===(null===(t=e.submenu)||void 0===t?void 0:t.id)})))||void 0===n?void 0:n.submenu;let d;const g=e.serviceManager.serverSettings;(0,r.requestTranslationsAPI)("","",{},g).then((e=>{for(const t in e.data){const n=e.data[t],i=n.displayName,r=n.nativeName,u=i===r,g=u?`${i}`:`${i} - ${r}`;d=`jupyterlab-translation:${t}`,l.addCommand(d,{label:g,caption:g,isEnabled:()=>!u,isVisible:()=>!0,isToggled:()=>u,execute:()=>(0,s.showDialog)({title:o.__("Change interface language?"),body:o.__("After changing the interface language to %1, you will need to reload JupyterLab to see the changes.",g),buttons:[s.Dialog.cancelButton({label:o.__("Cancel")}),s.Dialog.okButton({label:o.__("Change and reload")})]}).then((e=>{e.button.accept&&a.set("locale",t).then((()=>{window.location.reload()})).catch((e=>{console.error(e)}))}))}),c&&c.addItem({command:d,args:{}})}})).catch((e=>{console.error(`Available locales errored!\n${e}`)}))})).catch((e=>{console.error(`The jupyterlab translation extension appears to be missing.\n${e}`)}))}},g=[u,d]}}]);
//# sourceMappingURL=1440.7b43723.js.map