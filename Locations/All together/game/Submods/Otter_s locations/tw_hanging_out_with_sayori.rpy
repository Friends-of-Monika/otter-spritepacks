#hanging-out-with-sayori, location submod by my-otter-self on reddit for MONIKA AFTER STORY

init -1 python:
    mas_background_def = MASFilterableBackground(
        "tw_hanging_out_with_sayori",
        "(TW) Hanging out with Sayori",
        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_tw_hanging_out_with_sayori_day",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_tw_hanging_out_with_sayori_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_tw_hanging_out_with_sayori_sunset",
            }),
        ),
        MASBackgroundFilterManager(
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            ),
            MASBackgroundFilterChunk(
                True,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_DAY,
                    60
                ),
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_SUNSET,
                    60,
                    30*60,
                    10,
                ),
            ),
            MASBackgroundFilterChunk(
                False,
                None,
                MASBackgroundFilterSlice.cachecreate(
                    store.mas_sprites.FLT_NIGHT,
                    60
                )
            )
        ),
        hide_calendar=True,
        unlocked=True,
        entry_pp=store.mas_background._def_background_entry,
        exit_pp=store.mas_background._def_background_exit,
    )

    #Now load data
    store.mas_background.loadMBGData()


init 1 python in mas_background:

    # verify all backgrounds
    for flt_bg in BACKGROUND_MAP.itervalues():
        flt_bg.verify()

image submod_tw_hanging_out_with_sayori_day = "mod_assets/location/tw_hanging_out_with_sayori/tw_hanging_out_with_sayori.png"
image submod_tw_hanging_out_with_sayori_night = MASFilteredSprite(
    store.mas_sprites.FLT_NIGHT,
    "mod_assets/location/tw_hanging_out_with_sayori/tw_hanging_out_with_sayori.png"
)
image submod_tw_hanging_out_with_sayori_sunset = MASFilteredSprite(
    store.mas_sprites.FLT_SUNSET,
    "mod_assets/location/tw_hanging_out_with_sayori/tw_hanging_out_with_sayori.png"
)

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
