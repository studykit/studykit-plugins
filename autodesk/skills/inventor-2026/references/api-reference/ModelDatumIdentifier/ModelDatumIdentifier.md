# ModelDatumIdentifier Object

Derived from: [ModelAnnotation](../ModelAnnotation/ModelAnnotation.md) Object

## Description

ModelDatumIdentifier Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ModelDatumIdentifier/ModelDatumIdentifier_Delete.md) | Method that deletes the ModelDimension. |
| [GetDisplayGeometry](../ModelDatumIdentifier/ModelDatumIdentifier_GetDisplayGeometry.md) | Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids. |
| [GetFilledAreaFacetsInfo](../ModelDatumIdentifier/ModelDatumIdentifier_GetFilledAreaFacetsInfo.md) | Returns facets’ coordinates of the filled areas of the annotation. |
| [GetReferenceKey](../ModelDatumIdentifier/ModelDatumIdentifier_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelDatumIdentifier/ModelDatumIdentifier_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../ModelDatumIdentifier/ModelDatumIdentifier_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CompositeAnnotation](../ModelDatumIdentifier/ModelDatumIdentifier_CompositeAnnotation.md) | Read-only property that returns the ModelCompositeAnnotation object if this annotation is a member of it. This returns Nothing if the IsMemberOfCompositeAnnotation returns False. |
| [Definition](../ModelDatumIdentifier/ModelDatumIdentifier_Definition.md) | Read-write property that gets and sets the definition associated with this symbol. |
| [HealthStatus](../ModelDatumIdentifier/ModelDatumIdentifier_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../ModelDatumIdentifier/ModelDatumIdentifier_InternalName.md) | Gets the internal name (GUID) of the model annotation. |
| [IsMemberOfCompositeAnnotation](../ModelDatumIdentifier/ModelDatumIdentifier_IsMemberOfCompositeAnnotation.md) | Returns whether this annotation is a member of a ModelCompositeAnnotation. |
| [IsOwnedByToleranceFeature](../ModelDatumIdentifier/ModelDatumIdentifier_IsOwnedByToleranceFeature.md) | Returns whether this annotation is owned by a ModelToleranceFeature. |
| [Name](../ModelDatumIdentifier/ModelDatumIdentifier_Name.md) | Read-write property that gets and sets the name of the annotation. |
| [OwnedByToleranceFeature](../ModelDatumIdentifier/ModelDatumIdentifier_OwnedByToleranceFeature.md) | Returns the owning ModelToleranceFeature object. |
| [Parent](../ModelDatumIdentifier/ModelDatumIdentifier_Parent.md) | Read-only property that returns the parent component definition of the object. |
| [TopToleranceFeature](../ModelDatumIdentifier/ModelDatumIdentifier_TopToleranceFeature.md) | Returns the top ModelToleranceFeature object. |
| [Type](../ModelDatumIdentifier/ModelDatumIdentifier_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../ModelDatumIdentifier/ModelDatumIdentifier_Visible.md) | Gets and sets the visibility of the annotation. |

## Accessed From

[ModelDatumIdentifierDefinition.Parent](../ModelDatumIdentifierDefinition/ModelDatumIdentifierDefinition_Parent.md), [ModelDatumIdentifierProxy.NativeObject](../ModelDatumIdentifierProxy/ModelDatumIdentifierProxy_NativeObject.md), [ModelDatumIdentifiers.Add](../ModelDatumIdentifiers/ModelDatumIdentifiers_Add.md), [ModelDatumIdentifiers.Item](../ModelDatumIdentifiers/ModelDatumIdentifiers_Item.md), [ModelFeatureControlFrameRow.PrimaryCompoundDatumIdentifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_PrimaryCompoundDatumIdentifier.md), [ModelFeatureControlFrameRow.PrimaryDatumIdentifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_PrimaryDatumIdentifier.md), [ModelFeatureControlFrameRow.SecondaryCompoundDatumIdentifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_SecondaryCompoundDatumIdentifier.md), [ModelFeatureControlFrameRow.SecondaryDatumIdentifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_SecondaryDatumIdentifier.md), [ModelFeatureControlFrameRow.TertiaryCompoundDatumIdentifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_TertiaryCompoundDatumIdentifier.md), [ModelFeatureControlFrameRow.TertiaryDatumIdentifier](../ModelFeatureControlFrameRow/ModelFeatureControlFrameRow_TertiaryDatumIdentifier.md)

## Derived Classes

[ModelDatumIdentifierProxy](../ModelDatumIdentifierProxy/ModelDatumIdentifierProxy.md)

## Version

Introduced in version 2018
