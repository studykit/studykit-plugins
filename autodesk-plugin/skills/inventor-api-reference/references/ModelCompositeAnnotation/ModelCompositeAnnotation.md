# ModelCompositeAnnotation Object

Derived from: [ModelAnnotation](../ModelAnnotation/ModelAnnotation.md) Object

## Description

The ModelCompositeAnnotation represents one or more ModelAnnotation objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ModelCompositeAnnotation/ModelCompositeAnnotation_Delete.md) | Method that deletes the ModelDimension. |
| [GetDisplayGeometry](../ModelCompositeAnnotation/ModelCompositeAnnotation_GetDisplayGeometry.md) | Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids. |
| [GetFilledAreaFacetsInfo](../ModelCompositeAnnotation/ModelCompositeAnnotation_GetFilledAreaFacetsInfo.md) | Returns facets’ coordinates of the filled areas of the annotation. |
| [GetReferenceKey](../ModelCompositeAnnotation/ModelCompositeAnnotation_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelCompositeAnnotation/ModelCompositeAnnotation_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../ModelCompositeAnnotation/ModelCompositeAnnotation_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ClientId](../ModelCompositeAnnotation/ModelCompositeAnnotation_ClientId.md) | Returns the string that uniquely identifies the client. |
| [CompositeAnnotation](../ModelCompositeAnnotation/ModelCompositeAnnotation_CompositeAnnotation.md) | Read-only property that returns the ModelCompositeAnnotation object if this annotation is a member of it. This returns Nothing if the IsMemberOfCompositeAnnotation returns False. |
| [Definition](../ModelCompositeAnnotation/ModelCompositeAnnotation_Definition.md) | Gets and sets the ModelCompositeAnnotationDefinition associative with this object. |
| [HealthStatus](../ModelCompositeAnnotation/ModelCompositeAnnotation_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../ModelCompositeAnnotation/ModelCompositeAnnotation_InternalName.md) | Gets the internal name (GUID) of the model annotation. |
| [IsMemberOfCompositeAnnotation](../ModelCompositeAnnotation/ModelCompositeAnnotation_IsMemberOfCompositeAnnotation.md) | Returns whether this annotation is a member of a ModelCompositeAnnotation. |
| [IsOwnedByToleranceFeature](../ModelCompositeAnnotation/ModelCompositeAnnotation_IsOwnedByToleranceFeature.md) | Returns whether this annotation is owned by a ModelToleranceFeature. |
| [Name](../ModelCompositeAnnotation/ModelCompositeAnnotation_Name.md) | Read-write property that gets and sets the name of the annotation. |
| [OwnedByToleranceFeature](../ModelCompositeAnnotation/ModelCompositeAnnotation_OwnedByToleranceFeature.md) | Returns the owning ModelToleranceFeature object. |
| [Parent](../ModelCompositeAnnotation/ModelCompositeAnnotation_Parent.md) | Read-only property that returns the parent component definition of the object. |
| [TopToleranceFeature](../ModelCompositeAnnotation/ModelCompositeAnnotation_TopToleranceFeature.md) | Returns the top ModelToleranceFeature object. |
| [Type](../ModelCompositeAnnotation/ModelCompositeAnnotation_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../ModelCompositeAnnotation/ModelCompositeAnnotation_Visible.md) | Gets and sets the visibility of the annotation. |

## Accessed From

[AngularModelDimension.CompositeAnnotation](../AngularModelDimension/AngularModelDimension_CompositeAnnotation.md), [AngularModelDimensionProxy.CompositeAnnotation](../AngularModelDimensionProxy/AngularModelDimensionProxy_CompositeAnnotation.md), [DiameterModelDimension.CompositeAnnotation](../DiameterModelDimension/DiameterModelDimension_CompositeAnnotation.md), [DiameterModelDimensionProxy.CompositeAnnotation](../DiameterModelDimensionProxy/DiameterModelDimensionProxy_CompositeAnnotation.md), [LinearModelDimension.CompositeAnnotation](../LinearModelDimension/LinearModelDimension_CompositeAnnotation.md), [LinearModelDimensionProxy.CompositeAnnotation](../LinearModelDimensionProxy/LinearModelDimensionProxy_CompositeAnnotation.md), [ModelAnnotation.CompositeAnnotation](../ModelAnnotation/ModelAnnotation_CompositeAnnotation.md), [ModelCompositeAnnotation.CompositeAnnotation](../ModelCompositeAnnotation/ModelCompositeAnnotation_CompositeAnnotation.md), [ModelCompositeAnnotationDefinition.Parent](../ModelCompositeAnnotationDefinition/ModelCompositeAnnotationDefinition_Parent.md), [ModelCompositeAnnotationProxy.CompositeAnnotation](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy_CompositeAnnotation.md), [ModelCompositeAnnotationProxy.NativeObject](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy_NativeObject.md), [ModelCompositeAnnotations.Add](../ModelCompositeAnnotations/ModelCompositeAnnotations_Add.md), [ModelCompositeAnnotations.Item](../ModelCompositeAnnotations/ModelCompositeAnnotations_Item.md), [ModelDatumIdentifier.CompositeAnnotation](../ModelDatumIdentifier/ModelDatumIdentifier_CompositeAnnotation.md), [ModelDatumIdentifierProxy.CompositeAnnotation](../ModelDatumIdentifierProxy/ModelDatumIdentifierProxy_CompositeAnnotation.md), [ModelDatumTarget.CompositeAnnotation](../ModelDatumTarget/ModelDatumTarget_CompositeAnnotation.md), [ModelDatumTargetProxy.CompositeAnnotation](../ModelDatumTargetProxy/ModelDatumTargetProxy_CompositeAnnotation.md), [ModelDimension.CompositeAnnotation](../ModelDimension/ModelDimension_CompositeAnnotation.md), [ModelFeatureControlFrame.CompositeAnnotation](../ModelFeatureControlFrame/ModelFeatureControlFrame_CompositeAnnotation.md), [ModelFeatureControlFrameProxy.CompositeAnnotation](../ModelFeatureControlFrameProxy/ModelFeatureControlFrameProxy_CompositeAnnotation.md), [ModelGeneralNote.CompositeAnnotation](../ModelGeneralNote/ModelGeneralNote_CompositeAnnotation.md), [ModelGeneralNoteProxy.CompositeAnnotation](../ModelGeneralNoteProxy/ModelGeneralNoteProxy_CompositeAnnotation.md), [ModelHoleThreadNote.CompositeAnnotation](../ModelHoleThreadNote/ModelHoleThreadNote_CompositeAnnotation.md), [ModelHoleThreadNoteProxy.CompositeAnnotation](../ModelHoleThreadNoteProxy/ModelHoleThreadNoteProxy_CompositeAnnotation.md), [ModelLeaderNote.CompositeAnnotation](../ModelLeaderNote/ModelLeaderNote_CompositeAnnotation.md), [ModelLeaderNoteProxy.CompositeAnnotation](../ModelLeaderNoteProxy/ModelLeaderNoteProxy_CompositeAnnotation.md), [ModelSurfaceTextureSymbol.CompositeAnnotation](../ModelSurfaceTextureSymbol/ModelSurfaceTextureSymbol_CompositeAnnotation.md), [ModelSurfaceTextureSymbolProxy.CompositeAnnotation](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy_CompositeAnnotation.md), [ModelWeldingSymbol.CompositeAnnotation](../ModelWeldingSymbol/ModelWeldingSymbol_CompositeAnnotation.md), [ModelWeldingSymbolProxy.CompositeAnnotation](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy_CompositeAnnotation.md), [RadiusModelDimension.CompositeAnnotation](../RadiusModelDimension/RadiusModelDimension_CompositeAnnotation.md), [RadiusModelDimensionProxy.CompositeAnnotation](../RadiusModelDimensionProxy/RadiusModelDimensionProxy_CompositeAnnotation.md)

## Derived Classes

[ModelCompositeAnnotationProxy](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy.md)

## Version

Introduced in version 2018
