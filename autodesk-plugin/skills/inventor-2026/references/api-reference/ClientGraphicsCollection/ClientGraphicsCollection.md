# ClientGraphicsCollection Object

## Description

The ClientGraphicsCollection object provides access to all of the existing objects associated with a graphics container.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../ClientGraphicsCollection/ClientGraphicsCollection_Add.md) | Method that creates a new ClientGraphics object. The identifier supplied needs to uniquely identify the client. The method will fail in the case where a ClientGraphics object with this ClientId already exists on the object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ClientGraphicsCollection/ClientGraphicsCollection_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../ClientGraphicsCollection/ClientGraphicsCollection_Count.md) | Property that returns the number of ClientGraphics objects associated with the graphic container. |
| [Item](../ClientGraphicsCollection/ClientGraphicsCollection_Item.md) | Returns an existing ClientGraphics object. |
| [NonTransacting](../ClientGraphicsCollection/ClientGraphicsCollection_NonTransacting.md) | Read-only property that returns whether the creation of this ClientGraphicsColection object and all its associated data is non-transacting. |
| [Parent](../ClientGraphicsCollection/ClientGraphicsCollection_Parent.md) | Property returns the logical parent of this object. This could currently be a ComponentDefinition or an AssemblyOccurrence. |
| [Type](../ClientGraphicsCollection/ClientGraphicsCollection_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyComponentDefinition.ClientGraphicsCollection](../AssemblyComponentDefinition/AssemblyComponentDefinition_ClientGraphicsCollection.md), [AssemblyDocument.NonTransactingClientGraphicsCollection](../AssemblyDocument/AssemblyDocument_NonTransactingClientGraphicsCollection.md), [ClientFeatureDefinition.ClientGraphicsCollection](../ClientFeatureDefinition/ClientFeatureDefinition_ClientGraphicsCollection.md), [ClientGraphics.Parent](../ClientGraphics/ClientGraphics_Parent.md), [ComponentDefinition.ClientGraphicsCollection](../ComponentDefinition/ComponentDefinition_ClientGraphicsCollection.md), [DetailDrawingView.ClientGraphicsCollection](../DetailDrawingView/DetailDrawingView_ClientGraphicsCollection.md), [Document.NonTransactingClientGraphicsCollection](../Document/Document_NonTransactingClientGraphicsCollection.md), [DrawingDocument.NonTransactingClientGraphicsCollection](../DrawingDocument/DrawingDocument_NonTransactingClientGraphicsCollection.md), [DrawingView.ClientGraphicsCollection](../DrawingView/DrawingView_ClientGraphicsCollection.md), [FlatPattern.ClientGraphicsCollection](../FlatPattern/FlatPattern_ClientGraphicsCollection.md), [PartComponentDefinition.ClientGraphicsCollection](../PartComponentDefinition/PartComponentDefinition_ClientGraphicsCollection.md), [PartDocument.NonTransactingClientGraphicsCollection](../PartDocument/PartDocument_NonTransactingClientGraphicsCollection.md), [PresentationDocument.NonTransactingClientGraphicsCollection](../PresentationDocument/PresentationDocument_NonTransactingClientGraphicsCollection.md), [PresentationScene.ClientGraphicsCollection](../PresentationScene/PresentationScene_ClientGraphicsCollection.md), [Publication.ClientGraphicsCollection](Publication_ClientGraphicsCollection.md), [SectionDrawingView.ClientGraphicsCollection](../SectionDrawingView/SectionDrawingView_ClientGraphicsCollection.md), [Sheet.ClientGraphicsCollection](../Sheet/Sheet_ClientGraphicsCollection.md), [SheetMetalComponentDefinition.ClientGraphicsCollection](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_ClientGraphicsCollection.md), [VirtualComponentDefinition.ClientGraphicsCollection](../VirtualComponentDefinition/VirtualComponentDefinition_ClientGraphicsCollection.md), [WeldmentComponentDefinition.ClientGraphicsCollection](../WeldmentComponentDefinition/WeldmentComponentDefinition_ClientGraphicsCollection.md), [WeldsComponentDefinition.ClientGraphicsCollection](../WeldsComponentDefinition/WeldsComponentDefinition_ClientGraphicsCollection.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics - image in point graphics](../../sample-programs/PointGraphics_SetCustomImage_Sample.md) | The following sample demonstrates creation of point client graphics with a custom image. |
| [Client graphics creation of 3D primitives](../../sample-programs/TransientBRep_CreateSolidCylinderCone_Sample.md) | This sample demonstrates the creation of 3D primitives (cylinder, cone, etc.) using client graphics. |
| [Create curve primitives](../../sample-programs/TransientGeometry_Sample.md) | This sample demonstrates the creation of curve primitives (lines, arcs, circles, etc.) using client graphics. |

## Version

Introduced in version 5
