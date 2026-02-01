# ModelFeatureControlFrame Object

Derived from: [ModelAnnotation](../ModelAnnotation/ModelAnnotation.md) Object

## Description

ModelFeatureControlFrame Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ModelFeatureControlFrame/ModelFeatureControlFrame_Delete.md) | Method that deletes the ModelDimension. |
| [GetDisplayGeometry](../ModelFeatureControlFrame/ModelFeatureControlFrame_GetDisplayGeometry.md) | Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids. |
| [GetFilledAreaFacetsInfo](../ModelFeatureControlFrame/ModelFeatureControlFrame_GetFilledAreaFacetsInfo.md) | Returns facets’ coordinates of the filled areas of the annotation. |
| [GetReferenceKey](../ModelFeatureControlFrame/ModelFeatureControlFrame_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelFeatureControlFrame/ModelFeatureControlFrame_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../ModelFeatureControlFrame/ModelFeatureControlFrame_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CompositeAnnotation](../ModelFeatureControlFrame/ModelFeatureControlFrame_CompositeAnnotation.md) | Read-only property that returns the ModelCompositeAnnotation object if this annotation is a member of it. This returns Nothing if the IsMemberOfCompositeAnnotation returns False. |
| [Definition](../ModelFeatureControlFrame/ModelFeatureControlFrame_Definition.md) | Read-write property that gets and sets the definition associated with this symbol. |
| [HealthStatus](../ModelFeatureControlFrame/ModelFeatureControlFrame_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../ModelFeatureControlFrame/ModelFeatureControlFrame_InternalName.md) | Gets the internal name (GUID) of the model annotation. |
| [IsMemberOfCompositeAnnotation](../ModelFeatureControlFrame/ModelFeatureControlFrame_IsMemberOfCompositeAnnotation.md) | Returns whether this annotation is a member of a ModelCompositeAnnotation. |
| [IsOwnedByToleranceFeature](../ModelFeatureControlFrame/ModelFeatureControlFrame_IsOwnedByToleranceFeature.md) | Returns whether this annotation is owned by a ModelToleranceFeature. |
| [Name](../ModelFeatureControlFrame/ModelFeatureControlFrame_Name.md) | Read-write property that gets and sets the name of the annotation. |
| [OwnedByToleranceFeature](../ModelFeatureControlFrame/ModelFeatureControlFrame_OwnedByToleranceFeature.md) | Returns the owning ModelToleranceFeature object. |
| [Parent](../ModelFeatureControlFrame/ModelFeatureControlFrame_Parent.md) | Read-only property that returns the parent component definition of the object. |
| [TopToleranceFeature](../ModelFeatureControlFrame/ModelFeatureControlFrame_TopToleranceFeature.md) | Returns the top ModelToleranceFeature object. |
| [Type](../ModelFeatureControlFrame/ModelFeatureControlFrame_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../ModelFeatureControlFrame/ModelFeatureControlFrame_Visible.md) | Gets and sets the visibility of the annotation. |

## Accessed From

[ModelFeatureControlFrameDefinition.Parent](../ModelFeatureControlFrameDefinition/ModelFeatureControlFrameDefinition_Parent.md), [ModelFeatureControlFrameProxy.NativeObject](../ModelFeatureControlFrameProxy/ModelFeatureControlFrameProxy_NativeObject.md), [ModelFeatureControlFrames.Add](../ModelFeatureControlFrames/ModelFeatureControlFrames_Add.md), [ModelFeatureControlFrames.Item](../ModelFeatureControlFrames/ModelFeatureControlFrames_Item.md)

## Derived Classes

[ModelFeatureControlFrameProxy](../ModelFeatureControlFrameProxy/ModelFeatureControlFrameProxy.md)

## Version

Introduced in version 2018
