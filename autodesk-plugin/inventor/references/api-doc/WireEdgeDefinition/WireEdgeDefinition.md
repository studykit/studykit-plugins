# WireEdgeDefinition Object

## Description

WireEdgeDefinition Object.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../WireEdgeDefinition/WireEdgeDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AssociativeID](../WireEdgeDefinition/WireEdgeDefinition_AssociativeID.md) | Gets and sets the associate ID of this edge. This ID will be transferred to the corresponding edge when this SurfaceBodyDefinition is used to create a SurfaceBody. It is used by Inventor as the identifier for the edge and is used for tracking this geometry f. |
| [EndVertex](../WireEdgeDefinition/WireEdgeDefinition_EndVertex.md) | Gets and sets the end vertex of the edge. This can be Nothing where no end vertex is specifically defined. |
| [IsParamReversed](../WireEdgeDefinition/WireEdgeDefinition_IsParamReversed.md) | Gets and sets if the orientation of this EdgeUse is in the same direction or not relative to the associated EdgeDefinition object. |
| [ModelSpaceCurve](../WireEdgeDefinition/WireEdgeDefinition_ModelSpaceCurve.md) | Gets and sets the definition of the edge in model space. This can be Nothing in the case where no model space geometry is specified for this edge. |
| [StartVertex](../WireEdgeDefinition/WireEdgeDefinition_StartVertex.md) | Gets and sets the starting vertex of the edge. This can be Nothing where no start vertex is specifically defined. |
| [Type](../WireEdgeDefinition/WireEdgeDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[WireEdgeDefinitions.Add](../WireEdgeDefinitions/WireEdgeDefinitions_Add.md), [WireEdgeDefinitions.Item](../WireEdgeDefinitions/WireEdgeDefinitions_Item.md)

## Version

Introduced in version 2013

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |