# LanguageTools.IsValidPrimaryModelState Method

Parent Object: [LanguageTools](../LanguageTools/LanguageTools.md)

## Description

Method that returns whether the input primary model state string is valid or not. The input primary model state string can be in any language that Inventor supports.

## Syntax

LanguageTools.**IsValidPrimaryModelState**( ***PrimaryName*** As String ) As Boolean

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PrimaryName | String | Input String value that specifies the primary model state string. This string can be in any language that Inventor supports. Below are the valid localized string for primary model state string in different languages: {"en-US", "[Primary]"}, {"ja-JP", "[プライマリ]"}, {"de-DE", "[Primär]"}, {"cs-CZ", "[Primární]"},  {"pl-PL", "[Główny]"},  {"ru-RU", "[Oсновной]"},  {"it-IT", "[Primario]"},  {"fr-FR", "[Principale]"},  {"es-ES", "[Principal]"},  {"pt-BR", "[Principal]"},  {"ko-KR", "[1차]"},  {"zh-CN", "[主要]"},  {"zh-TW", "[主要]"}. |

## Version

Introduced in version 2023
