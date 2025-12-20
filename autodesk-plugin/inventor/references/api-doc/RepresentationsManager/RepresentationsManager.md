# RepresentationsManager Object

## Description

The RepresentationsManager object provides access to all types of representations in an assembly, and design view representations in a part.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [ActiveDesignViewRepresentation](../RepresentationsManager/RepresentationsManager_ActiveDesignViewRepresentation.md) | Property that returns the active DesignViewRepresentation object. |
| [ActivePositionalRepresentation](../RepresentationsManager/RepresentationsManager_ActivePositionalRepresentation.md) | Property that returns the active PositionalRepresentation object. This property returns Nothing in part documents. |
| [Application](../RepresentationsManager/RepresentationsManager_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DesignViewRepresentations](../RepresentationsManager/RepresentationsManager_DesignViewRepresentations.md) | Property that returns the DesignViewRepresentations collection object. |
| [Parent](../RepresentationsManager/RepresentationsManager_Parent.md) | Property that returns the parent AssemblyComponentDefinition object. |
| [PositionalRepresentations](../RepresentationsManager/RepresentationsManager_PositionalRepresentations.md) | Property that returns the PositionalRepresentations collection object. This property returns Nothing in part documents. |
| [Type](../RepresentationsManager/RepresentationsManager_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[AssemblyComponentDefinition.RepresentationsManager](../AssemblyComponentDefinition/AssemblyComponentDefinition_RepresentationsManager.md), [DesignViewRepresentation.Parent](../DesignViewRepresentation/DesignViewRepresentation_Parent.md), [FlatPattern.RepresentationsManager](../FlatPattern/FlatPattern_RepresentationsManager.md), [LevelOfDetailRepresentation.Parent](LevelOfDetailRepresentation_Parent.md), [PartComponentDefinition.RepresentationsManager](../PartComponentDefinition/PartComponentDefinition_RepresentationsManager.md), [PositionalRepresentation.Parent](../PositionalRepresentation/PositionalRepresentation_Parent.md), [SheetMetalComponentDefinition.RepresentationsManager](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_RepresentationsManager.md), [WeldmentComponentDefinition.RepresentationsManager](../WeldmentComponentDefinition/WeldmentComponentDefinition_RepresentationsManager.md)

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |