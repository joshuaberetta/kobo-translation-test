# Transcription et traduction de réponses audio

<iframe src="https://www.youtube.com/embed/vefmH9JzJTU?si=8aF_U8M6BAft9kRr" style="width: 100%; aspect-ratio: 16 / 9; height: auto; border: 0;" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

Les outils de traitement du langage naturel de KoboToolbox vous aident à collecter, gérer et analyser des données qualitatives plus efficacement. Ces outils incluent la transcription automatique de la parole en texte et la traduction automatique, avec une analyse qualitative automatisée à venir prochainement. La transcription originale de vos fichiers audio et tous les textes traduits sont ajoutés en tant que nouvelles colonnes de données dans le tableau de données et peuvent être [téléchargés](../fr/export_download.html) avec vos données d'enquête.

Pour utiliser ces fonctionnalités, collectez d'abord des réponses audio dans votre formulaire en utilisant le [type de question Audio](../fr/photo_audio_video_file.html) ou les [enregistrements audio d'arrière-plan](../fr/recording-interviews.html).

<p class="note">
    <strong>Remarque</strong> : La transcription et la traduction automatiques peuvent ne pas être disponibles pour <a href="#liste-des-langues">toutes les langues</a>. Pour ces langues, seules la transcription et la traduction manuelles sont possibles.
</p>

## Ajouter des transcriptions automatiques

![Exemple d'ajout de transcriptions automatiques](images/transcription_translation/transcription.png)

Pour commencer à transcrire vos réponses audio :

1. Ouvrez votre projet et accédez à **DONNÉES > Tableau**.
2. Appuyez sur le bouton **Ouvrir** à côté de la réponse audio que vous souhaitez transcrire.
3. Dans l'onglet **TRANSCRIPTION**, appuyez sur **begin**.
    - Sélectionnez la langue d'origine du fichier audio et l'option **automatic** (l'option **manual** vous permettra de transcrire manuellement l'enregistrement audio).
    - Appuyez sur **create transcript** pour commencer la transcription automatique.
4. Une fois la transcription terminée, vous pouvez la modifier manuellement. Vous pouvez lire l'enregistrement audio dans le coin supérieur droit pour vérifier l'exactitude de la transcription.
    - Après avoir modifié la transcription, appuyez sur le bouton **Save** pour vous assurer que votre travail est enregistré en toute sécurité.
5. Lorsque vous avez terminé, appuyez sur **DONE** pour quitter, accédez à la soumission suivante en appuyant sur les flèches à côté du bouton **DONE**, ou passez à l'onglet **TRANSLATIONS**.
    - Si vous appuyez sur **DONE**, vous serez redirigé(e) vers l'affichage du tableau de données, où une nouvelle colonne contenant la transcription aura été ajoutée.

<p class="note">
    <strong>Remarque</strong> : Les transcriptions et traductions générées automatiquement doivent être sauvegardées pour éviter toute perte de données. Quitter la page sans sauvegarder entraînera la perte des données.
</p>

## Ajouter des traductions automatiques

![Exemple d'ajout de traductions automatiques](images/transcription_translation/translation.png)

Une fois que vous avez une transcription complète de votre réponse audio, vous pouvez ajouter des traductions dans plusieurs langues :

1. Passez à l'onglet **TRANSLATIONS**.
    - L'option de traduction n'est disponible qu'une fois qu'une transcription a été complétée.
2. Appuyez sur **begin** et choisissez la langue de la traduction.
    - Appuyez sur **automatic** pour la traduction automatique (l'option **manual** vous permettra de traduire manuellement la transcription)
    - Appuyez sur **create translation** pour commencer la traduction automatique
3. Une fois la traduction terminée, vous pouvez la modifier manuellement. La transcription originale apparaît à droite de l'écran, et l'audio original apparaît en dessous.
    - Après avoir modifié la traduction, appuyez sur le bouton **Save** pour vous assurer que votre travail est enregistré en toute sécurité.
4. Lorsque la traduction est terminée, vous pouvez ajouter une autre traduction en appuyant sur <i class="k-icon-plus"></i> **new translation**, passer à la soumission suivante en appuyant sur les flèches à côté du numéro d'élément dans le coin supérieur droit, ou appuyer sur **DONE** pour revenir au tableau de données.

<p class="note">
    <strong>Remarque</strong> : Les fichiers audio ne peuvent contenir qu'une seule transcription, mais chaque transcription peut avoir plusieurs traductions.
</p>

## Liste des langues

Ces fonctionnalités de traitement du langage naturel intègrent des capacités de reconnaissance vocale automatique (ASR) et de traduction automatique (MT) fournies par Google Cloud Compute, qui offre actuellement la transcription automatique dans 72 langues (avec 138 variantes régionales) et la traduction automatique dans 106 langues. Pour la transcription ou la traduction manuelle, vous pouvez sélectionner parmi environ 7 000 langues basées sur la liste complète ISO 639-3, maintenue par SIL International (filtrée pour les « langues vivantes »). Si une langue prend en charge l'ASR ou la MT, vous pouvez choisir entre les méthodes **manual** et **automatic**. Pour les autres langues, seule la méthode **manual** est disponible.

Si vous ne trouvez pas une langue dans la liste, envisagez des orthographes ou des noms alternatifs. Tous les noms de langues sont actuellement listés en utilisant leurs noms et orthographes anglais (par exemple, Spanish au lieu d'Español). Pour les langues avec moins de locuteur(rice)s, il peut y avoir des noms alternatifs. Par exemple, la langue Bura du nord du Nigeria est listée comme Bura-Pabir mais est également connue sous le nom de Bourrah ou Babir.

<p class="note">
    <strong>Remarque</strong> : Lors de la transcription manuelle de réponses audio, il est important de sélectionner la langue correcte. Si la transcription générée manuellement ne correspond pas exactement à la langue ou à la région choisie, les traductions automatiques ultérieures utilisant cette transcription peuvent être incorrectes et produire des inexactitudes.
</p>

## Résolution de problèmes

<details>
    <summary><strong>La traduction ne se charge pas</strong></summary>
    Parfois, la deuxième traduction peut rester bloquée avec une icône de chargement. Si cela se produit, rafraîchissez la page et la traduction devrait apparaître. Il s'agit d'un problème que nous travaillons à résoudre.
</details>