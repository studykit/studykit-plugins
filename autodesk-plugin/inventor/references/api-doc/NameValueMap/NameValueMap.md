# NameValueMap Object

## Description

The NameValueMap object. This object provides context-specific information, usually the context in which an event occurred. For more information, see the Event Context Information article in the overview section.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../NameValueMap/NameValueMap_Add.md) | Add a value associated to the specified key name. |
| [Clear](../NameValueMap/NameValueMap_Clear.md) | Removes all objects from the map. |
| [Insert](../NameValueMap/NameValueMap_Insert.md) | Insert a name value pair into the name value map with specified location. |
| [Remove](../NameValueMap/NameValueMap_Remove.md) | Removes the specified object from the map. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Count](../NameValueMap/NameValueMap_Count.md) | Property that returns the count of name - value pairs in the map. |
| [Item](../NameValueMap/NameValueMap_Item.md) | Gets the value at the specified index number or key name. |
| [Name](../NameValueMap/NameValueMap_Name.md) | Property that returns the name associated with the specified integer index. |
| [Value](../NameValueMap/NameValueMap_Value.md) | Gets and sets the value of the item associated with the specified name. If the item with the specified name does not exist, it is added to the map. |

## Accessed From

[AssemblyDocument.GetSelectedObject](../AssemblyDocument/AssemblyDocument_GetSelectedObject.md), [ControlDefinitionEvents.FireOnCommandInputs](ControlDefinitionEvents_FireOnCommandInputs.md), [ControlDefinitionEvents.OnCommandInputs](ControlDefinitionEvents_OnCommandInputs.md), [DSValueGraph.GetSegmentInterpolationType](../DSValueGraph/DSValueGraph_GetSegmentInterpolationType.md), [FileDialog.OptionValues](../FileDialog/FileDialog_OptionValues.md), [FileManager.GetRevitEngineInstallationStatus](../FileManager/FileManager_GetRevitEngineInstallationStatus.md), [OnFaceCurve.Faces](../OnFaceCurve/OnFaceCurve_Faces.md), [OnFaceCurveProxy.Faces](../OnFaceCurveProxy/OnFaceCurveProxy_Faces.md), [PartDocument.GetSelectedObject](../PartDocument/PartDocument_GetSelectedObject.md), [PartsListFilterItem.Options](../PartsListFilterItem/PartsListFilterItem_Options.md), [RigidBodyJoint.GetJointData](RigidBodyJoint_GetJointData.md), [SurfaceBodyDefinition.CreateTransientSurfaceBody](../SurfaceBodyDefinition/SurfaceBodyDefinition_CreateTransientSurfaceBody.md), [TransientObjects.CreateNameValueMap](../TransientObjects/TransientObjects_CreateNameValueMap.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creation a balloon](../../sample-programs/Balloons_Add_Sample.md) | This sample demonstrates the creation of a balloon. |
| [Export to IFC Format Sample](../../sample-programs/ExportToIFCFormatSample_Sample.md) | This sample demonstrates how to export an assembly to IFC format. |
| [Open a Catia file using the Catia Translator Sample](../../sample-programs/ImportCatiaTranslator_Sample.md) | This sample demonstrates how open an Catia file using the Catia translator add-in. |
| [Open an NX file suing the NX Translator Sample](../../sample-programs/ImportNXTranslator_Sample.md) | This sample demonstrates how open an NX file using the NX translator add-in. |
| [Open Rhino Translator Sample](../../sample-programs/ImportRhinoTranslator_Sample.md) | This sample demonstrates how to opening a Rhino file using the Rhino translator add-in. |
| [Open an STL file using the STL Translator Sample](../../sample-programs/ImportSTLslator_Sample.md) | This sample demonstrates how open an STL file using the STL translator add-in. |
| [Create assembly occurrence with representations](../../sample-programs/OccurrenceAddWithOptions_Sample.md) | This sample demonstrates how to create an assembly occurrence by specifying various representations. |
| [Save as DWF Translator Sample](../../sample-programs/SaveAsDWFTranslator_Sample.md) | This sample demonstrates how to save a DWF file using the DWF translator add-in. |
| [Save as DWG Translator Sample](../../sample-programs/SaveAsDWGTranslator_Sample.md) | This sample demonstrates how to save a DWG file using the DWG translator add-in. |
| [Save as DXF Translator Sample](../../sample-programs/SaveAsDXFTranslator_Sample.md) | This sample demonstrates how to save a DXF file using the DXF translator add-in. |
| [Save as IGES Translator Sample](../../sample-programs/SaveAsIGESTranslator_Sample.md) | This sample demonstrates how to save a IGES file using the IGES translator add-in. |
| [Save as PDF Translator Sample](../../sample-programs/SaveAsPDFTranslator_Sample.md) | This sample demonstrates how to save a PDF file using the PDF translator add-in. |
| [Save as STEP Translator Sample](../../sample-programs/SaveAsSTEPTranslator_Sample.md) | This sample demonstrates how to save a STEP file using the STEP translator add-in. |
| [Transient solid body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody_Sample.md) | The following sample demonstrates the creation of a transient solid block body. The newly created body is then displayed using client graphics in a part. |
| [Transient surface body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody2_Sample.md) | The following sample demonstrates the creation of a transient surface body consisting of a single rectangular face. The body is created in transient space and then copied over to a part document as a base feature. |
| [Export to DWF](../../sample-programs/TranslatorAddIn_Sample.md) | This sample demonstrates publishing of Inventor files in DWF format. |
| [Export to DWG](../../sample-programs/TranslatorAddIn2_Sample.md) | This sample uses the DWG Translator Addin to publish to DWG. |
| [Export to DXF](../../sample-programs/TranslatorAddIn3_Sample.md) | This sample uses the DXF Translator Addin to publish to DXF. |
| [Export to IGES](../../sample-programs/TranslatorAddIn4_Sample.md) | This sample demonstrates exporting of Inventor files in IGES format. |
| [Export to STEP](../../sample-programs/TranslatorAddIn5_Sample.md) | This sample demonstrates exporting of Inventor files in STEP format. |
| [Export to PDF](../../sample-programs/TranslatorAddIn6_Sample.md) | This sample demonstrates exporting of Inventor files in PDF format. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |