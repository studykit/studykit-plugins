# TranslatorAddIn.HasOpenOptions Property

Parent Object: [TranslatorAddIn](../TranslatorAddIn/TranslatorAddIn.md)

## Description

Gets whether the translator has options available for opening the specified data-source.

## Remarks

See the various sample programs and the [Translator Options](TranslatorSettings.md) page for more information.

## Syntax

TranslatorAddIn.**HasOpenOptions**( ***SourceData*** As [DataMedium](../DataMedium/DataMedium.md), ***Context*** As [TranslationContext](../TranslationContext/TranslationContext.md), ***DefaultOptions*** As [NameValueMap](../NameValueMap/NameValueMap.md) ) As Boolean

## Property Value

This is a read only property whose value is a Boolean.

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SourceData | [DataMedium](../DataMedium/DataMedium.md) | Input DataMedium object that specifies the data source. |
| Context | [TranslationContext](../TranslationContext/TranslationContext.md) | Input TranslationContext object that can be used to determine the context for the translation. |
| DefaultOptions | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap that specifies default translation options. |

## Version

Introduced in version 4
