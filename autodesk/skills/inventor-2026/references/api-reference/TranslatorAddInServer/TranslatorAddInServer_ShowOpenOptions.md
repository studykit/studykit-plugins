# TranslatorAddInServer.ShowOpenOptions Method

Parent Object: [TranslatorAddInServer](../TranslatorAddInServer/TranslatorAddInServer.md)

## Description

Show the open options for the specified data-source. This method is only called if True was returned from HasOpenOptions.

## Syntax

TranslatorAddInServer.**ShowOpenOptions**( ***SourceData*** As [DataMedium](../DataMedium/DataMedium.md), ***Context*** As [TranslationContext](../TranslationContext/TranslationContext.md), ***ChosenOptions*** As [NameValueMap](../NameValueMap/NameValueMap.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SourceData | [DataMedium](../DataMedium/DataMedium.md) | Input DataMedium object that specifies the data source. |
| Context | [TranslationContext](../TranslationContext/TranslationContext.md) | Input TranslationContext object that can be used to determine the context for the translation. |
| ChosenOptions | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap that specifies the options chosen. |

## Version

Introduced in version 4
