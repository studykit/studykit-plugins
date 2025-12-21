# AnnotationPlaneDefinition Object

## Description

The AnnotationPlaneDefinition object represents the information used to define an annotation plane. It’s not the actual annotation plane, but only the definition of a plane.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AnnotationPlaneToModel](../AnnotationPlaneDefinition/AnnotationPlaneDefinition_AnnotationPlaneToModel.md) | Method that takes a 2d coordinate in annotation plane space, and returns a Point3d containing the coordinates of the point in model space. |
| [Copy](../AnnotationPlaneDefinition/AnnotationPlaneDefinition_Copy.md) | Method that creates a copy of this AnnotationPlaneDefinition object. The new AnnotationPlaneDefinition object is independent any annotation plane. It can edited and used as input to edit an existing annotation plane or to create a new annotation plane. |
| [ModelToAnnotationPlane](../AnnotationPlaneDefinition/AnnotationPlaneDefinition_ModelToAnnotationPlane.md) | Method that takes a 3d coordinate in model space, projects it onto the annotation plane along the normal of the plane and returns a Point2d object containing the resulting coordinate point in annotation plane space. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../AnnotationPlaneDefinition/AnnotationPlaneDefinition_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Origin](../AnnotationPlaneDefinition/AnnotationPlaneDefinition_Origin.md) | Read-only property that returns origin of the annotation plane in model space. |
| [Parent](../AnnotationPlaneDefinition/AnnotationPlaneDefinition_Parent.md) | Read-only property that returns the parent annotation plane this definition is associated with. This property can be Nothing in the case the definition was created using either the CreateAnnotationPlaneDefinitionUsingIntents or CreateAnnotationPlaneDefinitionUsingPlane methods of the ModelAnnotations object. |
| [PlanarEntity](../AnnotationPlaneDefinition/AnnotationPlaneDefinition_PlanarEntity.md) | Read-only property that returns the planar entity the annotation plane is associated with. This property can return Nothing in the case it’s not associated with a planar entity. |
| [Plane](../AnnotationPlaneDefinition/AnnotationPlaneDefinition_Plane.md) | Read-only property that returns the plane geometry indicating the position and orientation of the annotation plane in model space. |
| [Transformation](../AnnotationPlaneDefinition/AnnotationPlaneDefinition_Transformation.md) | Read-only property that returns a matrix indicating the position and orientation of the annotation plane in model space. |
| [Type](../AnnotationPlaneDefinition/AnnotationPlaneDefinition_Type.md) | Read-only property returning kAnnotationPlaneDefinitionObject indicating this object’s type. |
| [XAxis](../AnnotationPlaneDefinition/AnnotationPlaneDefinition_XAxis.md) | Read-only property that returns the orientation of the x axis of the annotation plane in model space. |
| [XAxisEntity](../AnnotationPlaneDefinition/AnnotationPlaneDefinition_XAxisEntity.md) | Read-write property that sets and gets the entity that defines the x axis of the annotation plane. |
| [XAxisRotation](../AnnotationPlaneDefinition/AnnotationPlaneDefinition_XAxisRotation.md) | Read-write property that gets and sets the rotation of the x-axis in radians against the XAxisEntity. Valid value is in (-Pi, Pi]. |

## Accessed From

[AngularModelDimensionDefinition.AnnotationPlaneDefinition](../AngularModelDimensionDefinition/AngularModelDimensionDefinition_AnnotationPlaneDefinition.md), [AnnotationPlane.Definition](../AnnotationPlane/AnnotationPlane_Definition.md), [AnnotationPlaneDefinition.Copy](../AnnotationPlaneDefinition/AnnotationPlaneDefinition_Copy.md), [AnnotationPlaneDefinitionsEnumerator.Item](../AnnotationPlaneDefinitionsEnumerator/AnnotationPlaneDefinitionsEnumerator_Item.md), [AnnotationPlaneProxy.Definition](../AnnotationPlaneProxy/AnnotationPlaneProxy_Definition.md), [DiameterModelDimensionDefinition.AnnotationPlaneDefinition](../DiameterModelDimensionDefinition/DiameterModelDimensionDefinition_AnnotationPlaneDefinition.md), [LinearModelDimensionDefinition.AnnotationPlaneDefinition](../LinearModelDimensionDefinition/LinearModelDimensionDefinition_AnnotationPlaneDefinition.md), [ModelAnnotations.CreateAnnotationPlaneDefinitionUsingPlane](../ModelAnnotations/ModelAnnotations_CreateAnnotationPlaneDefinitionUsingPlane.md), [ModelDatumIdentifierDefinition.AnnotationPlaneDefinition](../ModelDatumIdentifierDefinition/ModelDatumIdentifierDefinition_AnnotationPlaneDefinition.md), [ModelDimensionDefinition.AnnotationPlaneDefinition](../ModelDimensionDefinition/ModelDimensionDefinition_AnnotationPlaneDefinition.md), [ModelFeatureControlFrameDefinition.AnnotationPlaneDefinition](../ModelFeatureControlFrameDefinition/ModelFeatureControlFrameDefinition_AnnotationPlaneDefinition.md), [ModelGeneralNoteDefinition.AnnotationPlaneDefinition](../ModelGeneralNoteDefinition/ModelGeneralNoteDefinition_AnnotationPlaneDefinition.md), [ModelHoleThreadNoteDefinition.AnnotationPlaneDefinition](../ModelHoleThreadNoteDefinition/ModelHoleThreadNoteDefinition_AnnotationPlaneDefinition.md), [ModelLeaderNoteDefinition.AnnotationPlaneDefinition](../ModelLeaderNoteDefinition/ModelLeaderNoteDefinition_AnnotationPlaneDefinition.md), [ModelSurfaceTextureSymbolDefinition.AnnotationPlaneDefinition](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_AnnotationPlaneDefinition.md), [ModelWeldingSymbolDefinitions.AnnotationPlaneDefinition](../ModelWeldingSymbolDefinitions/ModelWeldingSymbolDefinitions_AnnotationPlaneDefinition.md), [RadiusModelDimensionDefinition.AnnotationPlaneDefinition](../RadiusModelDimensionDefinition/RadiusModelDimensionDefinition_AnnotationPlaneDefinition.md)

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |