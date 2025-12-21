# TranslatorAddIn.HasSaveCopyAsOptions Property

Parent Object: [TranslatorAddIn](../TranslatorAddIn/TranslatorAddIn.md)

## Description

Gets whether the translator has options available for saving the specified data-source.

## Remarks

See the various sample programs and the [Translator Options](TranslatorSettings.md) page for more information.

## Syntax

TranslatorAddIn.**HasSaveCopyAsOptions**( ***SourceObject*** As Object, ***Context*** As [TranslationContext](../TranslationContext/TranslationContext.md), ***DefaultOptions*** As [NameValueMap](../NameValueMap/NameValueMap.md) ) As Boolean

## Property Value

This is a read only property whose value is a Boolean.

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| SourceObject | Object | Document or FlatPattern that specifies the source of the data. FlatPattern can be exported to DXF, DWG, STEP and IGES formats. |
| Context | [TranslationContext](../TranslationContext/TranslationContext.md) | Input TranslationContext object that can be used to determine the context for the translation. |
| DefaultOptions | [NameValueMap](../NameValueMap/NameValueMap.md) | Input NameValueMap that specifies default translation options. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Save as DWF Translator Sample](../../sample-programs/SaveAsDWFTranslator_Sample.md) | This sample demonstrates how to save a DWF file using the DWF translator add-in. |
| [Save as DWG Translator Sample](../../sample-programs/SaveAsDWGTranslator_Sample.md) | This sample demonstrates how to save a DWG file using the DWG translator add-in. |
| [Save as DXF Translator Sample](../../sample-programs/SaveAsDXFTranslator_Sample.md) | This sample demonstrates how to save a DXF file using the DXF translator add-in. |
| [Save as IGES Translator Sample](../../sample-programs/SaveAsIGESTranslator_Sample.md) | This sample demonstrates how to save a IGES file using the IGES translator add-in. |
| [Save as PDF Translator Sample](../../sample-programs/SaveAsPDFTranslator_Sample.md) | This sample demonstrates how to save a PDF file using the PDF translator add-in. |
| [Save as STEP Translator Sample](../../sample-programs/SaveAsSTEPTranslator_Sample.md) | This sample demonstrates how to save a STEP file using the STEP translator add-in. |
| [Export to DWF](../../sample-programs/TranslatorAddIn_Sample.md) | This sample demonstrates publishing of Inventor files in DWF format. |
| [Export to DWG](../../sample-programs/TranslatorAddIn2_Sample.md) | This sample uses the DWG Translator Addin to publish to DWG. |
| [Export to DXF](../../sample-programs/TranslatorAddIn3_Sample.md) | This sample uses the DXF Translator Addin to publish to DXF. |
| [Export to IGES](../../sample-programs/TranslatorAddIn4_Sample.md) | This sample demonstrates exporting of Inventor files in IGES format. |
| [Export to STEP](../../sample-programs/TranslatorAddIn5_Sample.md) | This sample demonstrates exporting of Inventor files in STEP format. |
| [Export to PDF](../../sample-programs/TranslatorAddIn6_Sample.md) | This sample demonstrates exporting of Inventor files in PDF format. |

## Version

Introduced in version 4
