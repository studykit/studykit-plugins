# TranslatorAddInServer.ShowSaveCopyAsOptions Method

Parent Object: [TranslatorAddInServer](../TranslatorAddInServer/TranslatorAddInServer.md)

## Description

Show the save options for the specified data-source. This method is only called if True was returned from HasSaveCopyAsOptions.

## Syntax

TranslatorAddInServer.**ShowSaveCopyAsOptions**( ***SourceObject*** As Object, ***Context*** As [TranslationContext](../TranslationContext/TranslationContext.md), ***ChosenOptions*** As [NameValueMap](../NameValueMap/NameValueMap.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SourceObject | Object | Input object that specifies the source of the data to show the save options for. |
| Context | [TranslationContext](../TranslationContext/TranslationContext.md) | Input TranslationContext object that can be used to determine the context for the translation. |
| ChosenOptions | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap that specifies the options chosen. |

## Version

Introduced in version 4
