# EdgeDefinition Object

## Description

The EdgeDefinition represents a transient definition of an Edge object.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../EdgeDefinition/EdgeDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AssociativeID](../EdgeDefinition/EdgeDefinition_AssociativeID.md) | Gets and sets the associate ID of this edge. This ID will be transferred to the corresponding edge when this SurfaceBodyDefinition is used to create a SurfaceBody. It is used by Inventor as the identifier for the edge and is used for tracking this geometry f. |
| [EndVertex](../EdgeDefinition/EdgeDefinition_EndVertex.md) | Gets and sets the end vertex of the edge. This can be Nothing where no end vertex is specifically defined. |
| [FaceOne](../EdgeDefinition/EdgeDefinition_FaceOne.md) | Gets and sets the associated FaceDefinition object. This is used in two cases. The first case is where the edge is being defined by a parameter space curve and this face defines the parameter space of the curve provided through the ParameterSpaceCurveOne pro. |
| [FaceTwo](../EdgeDefinition/EdgeDefinition_FaceTwo.md) | Gets and sets the associated FaceDefinition object. This is used in two cases. The first case is where the edge is being defined by a parameter space curve and this face defines the parameter space of the curve provided through the ParameterSpaceCurveTwo pro. |
| [IsParamReversed](../EdgeDefinition/EdgeDefinition_IsParamReversed.md) | Gets and sets if the orientation of this EdgeUse is in the same direction or not relative to the associated EdgeDefinition object. |
| [ModelSpaceCurve](../EdgeDefinition/EdgeDefinition_ModelSpaceCurve.md) | Gets and sets the definition of the edge in model space. This can be Nothing in the case where no model space geometry is specified for this edge. |
| [ParameterSpaceCurveOne](../EdgeDefinition/EdgeDefinition_ParameterSpaceCurveOne.md) | Gets and sets the definition of the edge in parameter space. If this is provided then the FaceOne property must also be set to define the parameter space this curve is defined within. This can be Nothing in the case where no parameter space curve is defined f. |
| [ParameterSpaceCurveTwo](../EdgeDefinition/EdgeDefinition_ParameterSpaceCurveTwo.md) | Gets and sets the definition of the edge in parameter space. If this is provided then the FaceTwo property must also be set to define the parameter space this curve is defined within. This can be Nothing in the case where no parameter space curve is defined f. |
| [StartVertex](../EdgeDefinition/EdgeDefinition_StartVertex.md) | Gets and sets the starting vertex of the edge. This can be Nothing where no start vertex is specifically defined. |
| [Type](../EdgeDefinition/EdgeDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[EdgeDefinitions.Add](../EdgeDefinitions/EdgeDefinitions_Add.md), [EdgeDefinitions.Item](../EdgeDefinitions/EdgeDefinitions_Item.md), [EdgeUseDefinition.EdgeDefinition](../EdgeUseDefinition/EdgeUseDefinition_EdgeDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Transient solid body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody_Sample.md) | The following sample demonstrates the creation of a transient solid block body. The newly created body is then displayed using client graphics in a part. |

## Version

Introduced in version 2011
