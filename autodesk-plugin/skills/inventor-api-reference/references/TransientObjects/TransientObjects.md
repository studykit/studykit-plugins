# TransientObjects Object

## Description

Object through which all general transient objects are constructed.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CreateCamera](../TransientObjects/TransientObjects_CreateCamera.md) | Constructs a new Camera object. |
| [CreateColor](../TransientObjects/TransientObjects_CreateColor.md) | Method to construct a new Color object. |
| [CreateDataMedium](../TransientObjects/TransientObjects_CreateDataMedium.md) | Method that constructs a new DataMedium object. |
| [CreateEdgeCollection](../TransientObjects/TransientObjects_CreateEdgeCollection.md) | Method creates a new EdgeCollection object. Optionally, the resulting EdgeCollection can be initialized with the contents of an enumerator containing edges that is passed in. Typically, an empty EdgeCollection will be created and populated using the Add method of the EdgeCollection object. |
| [CreateFaceCollection](../TransientObjects/TransientObjects_CreateFaceCollection.md) | Constructs a new FaceCollection object. If an ObjectsEnumerator is passed in, the collection starts off containing the enumerated objects. |
| [CreateFileMetadata](../TransientObjects/TransientObjects_CreateFileMetadata.md) | Method that creates a new FileMetadata object. The newly created FileMetadata is returned. |
| [CreateNameValueMap](../TransientObjects/TransientObjects_CreateNameValueMap.md) | Constructs a new NameValueMap object. |
| [CreateObjectCollection](../TransientObjects/TransientObjects_CreateObjectCollection.md) | Constructs a new ObjectCollection object. If an ObjectsEnumerator is passed in, the collection starts off containing the enumerated objects. |
| [CreateObjectCollectionByVariant](../TransientObjects/TransientObjects_CreateObjectCollectionByVariant.md) | Constructs a new ObjectCollectionByVariant object. If an ObjectsEnumeratorByVariant is passed in, the collection starts off containing the enumerated objects. |
| [CreateSignatureString](../TransientObjects/TransientObjects_CreateSignatureString.md) | Constructs a unique signature for a string. |
| [CreateTranslationContext](../TransientObjects/TransientObjects_CreateTranslationContext.md) | Constructs a new TranslationContext object, used in TranslatorAddin workflows. |

## Accessed From

[Application.TransientObjects](../Application/Application_TransientObjects.md), [ApprenticeServer.TransientObjects](../ApprenticeServer/ApprenticeServer_TransientObjects.md), [ApprenticeServerComponent.TransientObjects](../ApprenticeServerComponent/ApprenticeServerComponent_TransientObjects.md), [InventorServer.TransientObjects](InventorServer_TransientObjects.md), [InventorServerObject.TransientObjects](InventorServerObject_TransientObjects.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creation a balloon](../../sample-programs/Balloons_Add_Sample.md) | This sample demonstrates the creation of a balloon. |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |
| [Chain dimensions sets](../../sample-programs/ChainDimensionSets_Add_Sample.md) | This sample demonstrates the creation of a chain dimension set in a drawing. |
| [Copy a sketch](../../sample-programs/CopySketch_Sample.md) | This sample demonstrates copying the contents of a sketch into another sketch via the API. |
| [Selectively link paramaters](../../sample-programs/DerivedParameterTables_Add2_Sample.md) | This sample demonstrates the selective linking of parameters from another Inventor file. |
| [Edit profile of an extrude feature](../../sample-programs/ExtrudeFeature_Profile_Sample.md) | This sample demonstrates editing the profile of an extrude feature. |
| [Modify Multiple Model States Sample](../../sample-programs/ModifyMultipleModelStatesSample_Sample.md) | This sample demonstrates how to set multiple but not all model states into edit mode. |
| [Add a punch tool feature](../../sample-programs/PunchToolFeatures_Add_Sample.md) | This program demonstrates the creation of a punch tool feature. It uses one of the punch features that's delivered with Inventor. It assumes you already have an existing sheet metal part and have selected a face to place the punch feature on. The selected face should be large so there is room for the punch features. |
| [Create a ribbon panel in an existing tab](../../sample-programs/RibbonPanels_Add_Sample.md) | Demonstrates creating a new ribbon panel within an existing ribbon tab. |
| [Create sheet metal face and flange features](../../sample-programs/SheetMetalFeatures_FlangeFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and flange features. |
| [Create sketched symbol and leader](../../sample-programs/SketchedSymbols_AddWithLeader_Sample.md) | This sample illustrates creating sketched symbol with a leader. |
| [Add surface texture symbol to dimension](../../sample-programs/SurfaceTextureSymbols_Add_Sample.md) | This sample demonstrates the creation of a surface texture symbol attached to the extension line of a drawing dimension. |
| [Export to DWF](../../sample-programs/TranslatorAddIn_Sample.md) | This sample demonstrates publishing of Inventor files in DWF format. |
| [Export to DWG](../../sample-programs/TranslatorAddIn2_Sample.md) | This sample uses the DWG Translator Addin to publish to DWG. |
| [Export to DXF](../../sample-programs/TranslatorAddIn3_Sample.md) | This sample uses the DXF Translator Addin to publish to DXF. |
| [Export to IGES](../../sample-programs/TranslatorAddIn4_Sample.md) | This sample demonstrates exporting of Inventor files in IGES format. |
| [Export to STEP](../../sample-programs/TranslatorAddIn5_Sample.md) | This sample demonstrates exporting of Inventor files in STEP format. |
| [Export to PDF](../../sample-programs/TranslatorAddIn6_Sample.md) | This sample demonstrates exporting of Inventor files in PDF format. |

## Version

Introduced in version 4
