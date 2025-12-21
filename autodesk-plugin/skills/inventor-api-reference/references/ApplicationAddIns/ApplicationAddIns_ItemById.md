# ApplicationAddIns.ItemById Property

Parent Object: [ApplicationAddIns](../ApplicationAddIns/ApplicationAddIns.md)

## Description

Returns the specified ApplicationAddIn object from the collection. Retrieves an ApplicationAddIn object based on the Client Id.

## Syntax

ApplicationAddIns.**ItemById**( ***ClientId*** As String ) As [ApplicationAddIn](../ApplicationAddIn/ApplicationAddIn.md)

## Property Value

This is a read only property whose value is an [ApplicationAddIn](../ApplicationAddIn/ApplicationAddIn.md).

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ClientId | String | Input String that specifies the ApplicationAddIn to return. This is a string indicating either the ClassId of the Add-in or the unique ClientId associated with the Add-in. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Export to IFC Format Sample](../../sample-programs/ExportToIFCFormatSample_Sample.md) | This sample demonstrates how to export an assembly to IFC format. |
| [Open a Catia file using the Catia Translator Sample](../../sample-programs/ImportCatiaTranslator_Sample.md) | This sample demonstrates how open an Catia file using the Catia translator add-in. |
| [Open an NX file suing the NX Translator Sample](../../sample-programs/ImportNXTranslator_Sample.md) | This sample demonstrates how open an NX file using the NX translator add-in. |
| [Open Rhino Translator Sample](../../sample-programs/ImportRhinoTranslator_Sample.md) | This sample demonstrates how to opening a Rhino file using the Rhino translator add-in. |
| [Open an STL file using the STL Translator Sample](../../sample-programs/ImportSTLslator_Sample.md) | This sample demonstrates how open an STL file using the STL translator add-in. |
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

Introduced in version 2008
