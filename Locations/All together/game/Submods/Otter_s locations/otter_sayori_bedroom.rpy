#sayori_bedroom, location submod by my-otter-self on reddit for MONIKA AFTER STORY

init -1 python:
    mas_background_def = MASFilterableBackground(
        "otter_sayori_bedroom",
        "Sayori's Bedroom",
        MASFilterWeatherMap(
            day=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_sayori_bedroom_day",
            }),
            night=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_sayori_bedroom_night",
            }),
            sunset=MASWeatherMap({
                store.mas_weather.PRECIP_TYPE_DEF: "submod_sayori_bedroom_sunset",
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

image submod_sayori_bedroom_day = "mod_assets/location/sayori_bedroom/sayori_bedroom_day.png"
image submod_sayori_bedroom_night = "mod_assets/location/sayori_bedroom/sayori_bedroom_night.png"
image submod_sayori_bedroom_sunset = MASFilteredSprite(
    store.mas_sprites.FLT_SUNSET,
    "mod_assets/location/sayori_bedroom/sayori_bedroom_day.png"
)

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!
