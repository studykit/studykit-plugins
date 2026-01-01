# TranslatorAddIn.Open Method

Parent Object: [TranslatorAddIn](../TranslatorAddIn/TranslatorAddIn.md)

## Description

Open the data specified by the data-source.

## Remarks

See the various sample programs and the [Translator Options](TranslatorSettings.md) page for more information.

## Syntax

TranslatorAddIn.**Open**( ***SourceData*** As [DataMedium](../DataMedium/DataMedium.md), ***Context*** As [TranslationContext](../TranslationContext/TranslationContext.md), ***Options*** As [NameValueMap](../NameValueMap/NameValueMap.md), ***TargetObject*** As Object )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SourceData | [DataMedium](../DataMedium/DataMedium.md) | Input DataMedium object that specifies the data source. |
| Context | [TranslationContext](../TranslationContext/TranslationContext.md) | Input TranslationContext object that can be used to determine the context for the translation. |
| Options | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap that specifies translation options. |
| TargetObject | Object | Output object in which to place the data from the data source. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Open a Catia file using the Catia Translator Sample](../../sample-programs/ImportCatiaTranslator_Sample.md) | This sample demonstrates how open an Catia file using the Catia translator add-in. |
| [Import DWG into sketch](../../sample-programs/ImportDWGIntoSketchSample_Sample.md) | This sample demonstrates how to import DWG into sketch. |
| [Open an NX file suing the NX Translator Sample](../../sample-programs/ImportNXTranslator_Sample.md) | This sample demonstrates how open an NX file using the NX translator add-in. |
| [Open Rhino Translator Sample](../../sample-programs/ImportRhinoTranslator_Sample.md) | This sample demonstrates how to opening a Rhino file using the Rhino translator add-in. |
| [Open an STL file using the STL Translator Sample](../../sample-programs/ImportSTLslator_Sample.md) | This sample demonstrates how open an STL file using the STL translator add-in. |

## Version

Introduced in version 4
