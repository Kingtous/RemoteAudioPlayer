#include <stdio.h>
#include <alsa/asoundlib.h>
 

void parseArgs(int argc,char ** argv,int *vol);

int main(int argc,char ** argv)
{

    int vol_add;
    parseArgs(argc,argv,&vol_add);
    int unmute, chn;
    int al, ar;
    snd_mixer_t *mixer;
    snd_mixer_elem_t *master_element;
    snd_mixer_open(&mixer, 0);
    snd_mixer_attach(mixer, "default");
    snd_mixer_selem_register(mixer, NULL, NULL);
    snd_mixer_load(mixer);  
    /* 取得第一個 element，也就是 Master */
    master_element = snd_mixer_first_elem(mixer);  
    /* 設定音量的範圍 0 ~ 100 */  
    snd_mixer_selem_set_playback_volume_range(master_element, 0, 100);  
    /* 取得左右聲道的音量 */  
    snd_mixer_selem_get_playback_volume(master_element,SND_MIXER_SCHN_FRONT_LEFT,&al);
    snd_mixer_selem_get_playback_volume(master_element,SND_MIXER_SCHN_FRONT_LEFT,&ar);
    printf("Master volume is %d\n", (al + ar) >> 1);  /* 設定 Master 音量 */  
    if (((al + ar) >> 1 + 10)>=100)
    {
      return 0;
    }
    snd_mixer_selem_set_playback_volume(master_element, SND_MIXER_SCHN_FRONT_LEFT, al+vol_add);  
    snd_mixer_selem_set_playback_volume(master_element, SND_MIXER_SCHN_FRONT_RIGHT, ar+vol_add);  
    /* 將 Master 切換為靜音 */  
    for (chn=0;chn<=SND_MIXER_SCHN_LAST;chn++) {      
      snd_mixer_selem_set_playback_switch(master_element, chn, 0);  
    }  /* 將 Master 切換為非靜音 */  
    for (chn=0;chn<=SND_MIXER_SCHN_LAST;chn++) {      
      snd_mixer_selem_set_playback_switch(master_element, chn, 1);  
    }  
    return 0;
}


void parseArgs(int argc,char ** argv,int *vol){
  if (argc != 2)
    {
      fprintf(stderr,"args error.");
      exit(-1);
    }
    char * argument = argv[1];
    if (!strncmp(argument,"-i",2))
    {
      *vol = 10;
    }
    else if (!strncmp(argument,"-d",2))
    {
      *vol = -10;
    }
    else{
      fprintf(stderr,"%s cannot be recognized.",argument);
      exit(-1);
    }
}