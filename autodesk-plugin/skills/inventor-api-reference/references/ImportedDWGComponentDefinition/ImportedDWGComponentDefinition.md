# ImportedDWGComponentDefinition Object

Derived from: [ImportedComponentDefinition](../ImportedComponentDefinition/ImportedComponentDefinition.md) Object

## Description

ImportedDWGComponentDefinition Collection Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../ImportedDWGComponentDefinition/ImportedDWGComponentDefinition_Copy.md) | Method that creates a copy of this ImportedDWGComponentDefinition object. |
| [SetLocation](../ImportedDWGComponentDefinition/ImportedDWGComponentDefinition_SetLocation.md) | Method that sets the plane and origin to define the location of the imported DWG component. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ImportedDWGComponentDefinition/ImportedDWGComponentDefinition_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [DWGReferenceOrigin](../ImportedDWGComponentDefinition/ImportedDWGComponentDefinition_DWGReferenceOrigin.md) | Read-write property that gets and sets the reference origin for the imported DWG component. |
| [DWGReferenceOriginInLocationPlane](../ImportedDWGComponentDefinition/ImportedDWGComponentDefinition_DWGReferenceOriginInLocationPlane.md) | Read-write property that gets and sets the position of the imported DWG component origin. |
| [DWGRotationInLocationPlane](../ImportedDWGComponentDefinition/ImportedDWGComponentDefinition_DWGRotationInLocationPlane.md) | Read-write property that gets and sets the absolute rotation angle of the imported DWG component in LocationPlane space. |
| [FullFileName](../ImportedDWGComponentDefinition/ImportedDWGComponentDefinition_FullFileName.md) | Read-only property that returns the full filename of the source file. |
| [ImportDWGBodyStyle](../ImportedDWGComponentDefinition/ImportedDWGComponentDefinition_ImportDWGBodyStyle.md) | Read-write property determines how solid and surface bodies are handled on import. |
| [LocationOrigin](../ImportedDWGComponentDefinition/ImportedDWGComponentDefinition_LocationOrigin.md) | Read-write property that gets and sets the object indicating the position for the origin of the imported DWG component. |
| [LocationPlane](../ImportedDWGComponentDefinition/ImportedDWGComponentDefinition_LocationPlane.md) | Read-write property that gets and sets the location plane for the imported DWG component. |
| [Parent](../ImportedDWGComponentDefinition/ImportedDWGComponentDefinition_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Transformation](../ImportedDWGComponentDefinition/ImportedDWGComponentDefinition_Transformation.md) | Read-write property that gets and sets the translation and rotation of the imported DWG in part space. |
| [Type](../ImportedDWGComponentDefinition/ImportedDWGComponentDefinition_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[ImportedDWGComponentDefinition.Copy](../ImportedDWGComponentDefinition/ImportedDWGComponentDefinition_Copy.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Associatively import AutoCAD](../../sample-programs/ImportedComponent_AutoCAD_DWG_Sample.md) | This sample demonstrates how to import AutoCAD associatively. |
| [ImportedDWGComponent Creation](../../sample-programs/ImportedDWGComponentCreation_Sample.md) | This sample demonstrates how to create an imported DWG component into Inventor part document, and project the DWG entities onto Inventor planar sketch. |

## Version

Introduced in version 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |