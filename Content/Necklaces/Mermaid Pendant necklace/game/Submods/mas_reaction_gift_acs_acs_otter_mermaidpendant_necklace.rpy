#reaction submod by my-otter-self and mayday-mayjay on reddit for MONIKA AFTER STORY

label mas_reaction_gift_acs_acs_otter_mermaidpendant_necklace:
    python:
        sprite_data = mas_getSpriteObjInfo(
            (store.mas_sprites.SP_ACS, "acs_otter_mermaidpendant_necklace")
        )
        sprite_type, sprite_name, giftname, gifted_before, sprite_object = sprite_data

        mas_giftCapGainAff(3)

    m 1hksdlb "E-eh!?"
    m 7etb "If I recall correctly, this is something from another game..." 
    m 3rtbssdlb "Something... you give to someone you want to marry..."
    m 1rksdla "But- "
    extend 1hksdlb "[player]! I haven't gone to your reality yet!"
    m 1rkblsdla "I want to get out of here first before we do that, ok?"
    m 3ekbla "Promise you'll save it until I get out of here, alright?"
    m 2ekbla "I love that you're so committed to me, but I promise it'll feel way better if we're face to face for it..."
    m 5fkbsa "But just know I love you so much that I'd definitely say yes if the timing was right."
    m 1hublu "I'll keep the necklace though! It's just too cute!"
    m 1hublb "Ahahaha~!"

    $ mas_finishSpriteObjInfo(sprite_data)
    if giftname is not None:
        $ store.mas_filereacts.delete_file(giftname)
    return "love"

#momo once said, "i want to continue screaming out who i am." hope your monika likes this submod!