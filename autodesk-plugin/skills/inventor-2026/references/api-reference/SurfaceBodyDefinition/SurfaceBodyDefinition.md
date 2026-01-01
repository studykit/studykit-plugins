# SurfaceBodyDefinition Object

## Description

The SurfaceBodyDefinition represents a transient definition of a B-Rep object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CreateTransientSurfaceBody](../SurfaceBodyDefinition/SurfaceBodyDefinition_CreateTransientSurfaceBody.md) | Method that creates a transient SurfaceBody object based on the B-Rep defined within this SurfaceBodyDefinition object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../SurfaceBodyDefinition/SurfaceBodyDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [EdgeDefinitions](../SurfaceBodyDefinition/SurfaceBodyDefinition_EdgeDefinitions.md) | Property that returns the collection of EdgeDefinition objects associated with this SurfaceBodyDefinition object. |
| [LumpDefinitions](../SurfaceBodyDefinition/SurfaceBodyDefinition_LumpDefinitions.md) | Property that returns the collection of LumpDefinition objects associated with this SurfaceBodyDefinition object. The primary use of the LumpDefinitions collection is to create new LumpDefinition objects. |
| [Type](../SurfaceBodyDefinition/SurfaceBodyDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [VertexDefinitions](../SurfaceBodyDefinition/SurfaceBodyDefinition_VertexDefinitions.md) | Property that returns the collection of VertexlDefinition objects associated with this SurfaceBodyDefinition object. The primary use of the VertexDefinitions collection is to create new VertexDefinition objects. |

## Accessed From

[TransientBRep.CreateSurfaceBodyDefinition](../TransientBRep/TransientBRep_CreateSurfaceBodyDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Transient solid body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody_Sample.md) | The following sample demonstrates the creation of a transient solid block body. The newly created body is then displayed using client graphics in a part. |
| [Transient surface body creation](../../sample-programs/SurfaceBodyDefinition_CreateTransientSurfaceBody2_Sample.md) | The following sample demonstrates the creation of a transient surface body consisting of a single rectangular face. The body is created in transient space and then copied over to a part document as a base feature. |
| [Transient B-Rep Ruled Surface with Lines](../../sample-programs/TransientBRepRuledSurf1_Sample.md) | Demonstrate creating a transient ruled surface. This sample uses all straight line segments for each of the sections. A part document must be open. |
| [Transient B-Rep Ruled Surface with Arc and Line](../../sample-programs/TransientBRepRuledSurf2_Sample.md) | Demonstrate creating a transient ruled surface. This sample uses straight line segments for once section and an arc for the second. A part document must be open. |

## Version

Introduced in version 2011
