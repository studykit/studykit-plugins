# ModelLeaderNote Object

Derived from: [ModelAnnotation](../ModelAnnotation/ModelAnnotation.md) Object

## Description

The ModelLeaderNote object represents a leader note in a part or assembly.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ModelLeaderNote/ModelLeaderNote_Delete.md) | Method that deletes the ModelDimension. |
| [GetDisplayGeometry](../ModelLeaderNote/ModelLeaderNote_GetDisplayGeometry.md) | Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids. |
| [GetFilledAreaFacetsInfo](../ModelLeaderNote/ModelLeaderNote_GetFilledAreaFacetsInfo.md) | Returns facets’ coordinates of the filled areas of the annotation. |
| [GetReferenceKey](../ModelLeaderNote/ModelLeaderNote_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelLeaderNote/ModelLeaderNote_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../ModelLeaderNote/ModelLeaderNote_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CompositeAnnotation](../ModelLeaderNote/ModelLeaderNote_CompositeAnnotation.md) | Read-only property that returns the ModelCompositeAnnotation object if this annotation is a member of it. This returns Nothing if the IsMemberOfCompositeAnnotation returns False. |
| [Definition](../ModelLeaderNote/ModelLeaderNote_Definition.md) | Read-write property that gets and sets the definition associated with this symbol. When reading this property, the definition returned remains associated to the dimension and any changes made to the definition will be immediately reflected in the dimension.To. |
| [HealthStatus](../ModelLeaderNote/ModelLeaderNote_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../ModelLeaderNote/ModelLeaderNote_InternalName.md) | Gets the internal name (GUID) of the model annotation. |
| [IsMemberOfCompositeAnnotation](../ModelLeaderNote/ModelLeaderNote_IsMemberOfCompositeAnnotation.md) | Returns whether this annotation is a member of a ModelCompositeAnnotation. |
| [IsOwnedByToleranceFeature](../ModelLeaderNote/ModelLeaderNote_IsOwnedByToleranceFeature.md) | Returns whether this annotation is owned by a ModelToleranceFeature. |
| [Name](../ModelLeaderNote/ModelLeaderNote_Name.md) | Read-write property that gets and sets the name of the annotation. |
| [OwnedByToleranceFeature](../ModelLeaderNote/ModelLeaderNote_OwnedByToleranceFeature.md) | Returns the owning ModelToleranceFeature object. |
| [Parent](../ModelLeaderNote/ModelLeaderNote_Parent.md) | Read-only property that returns the parent component definition of the object. |
| [TopToleranceFeature](../ModelLeaderNote/ModelLeaderNote_TopToleranceFeature.md) | Returns the top ModelToleranceFeature object. |
| [Type](../ModelLeaderNote/ModelLeaderNote_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../ModelLeaderNote/ModelLeaderNote_Visible.md) | Gets and sets the visibility of the annotation. |

## Accessed From

[ModelLeaderNoteProxy.NativeObject](../ModelLeaderNoteProxy/ModelLeaderNoteProxy_NativeObject.md), [ModelLeaderNotes.Add](../ModelLeaderNotes/ModelLeaderNotes_Add.md), [ModelLeaderNotes.Item](../ModelLeaderNotes/ModelLeaderNotes_Item.md)

## Derived Classes

[ModelLeaderNoteProxy](../ModelLeaderNoteProxy/ModelLeaderNoteProxy.md)

## Version

Introduced in version 2018
