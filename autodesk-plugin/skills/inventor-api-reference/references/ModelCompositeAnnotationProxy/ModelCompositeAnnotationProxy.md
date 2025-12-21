# ModelCompositeAnnotationProxy Object

Derived from: [ModelCompositeAnnotation](../ModelCompositeAnnotation/ModelCompositeAnnotation.md) Object

## Description

ModelCompositeAnnotationProxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy_Delete.md) | Method that deletes the ModelDimension. |
| [GetDisplayGeometry](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy_GetDisplayGeometry.md) | Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids. |
| [GetFilledAreaFacetsInfo](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy_GetFilledAreaFacetsInfo.md) | Returns facets’ coordinates of the filled areas of the annotation. |
| [GetReferenceKey](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ClientId](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy_ClientId.md) | Returns the string that uniquely identifies the client. |
| [CompositeAnnotation](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy_CompositeAnnotation.md) | Read-only property that returns the ModelCompositeAnnotation object if this annotation is a member of it. This returns Nothing if the IsMemberOfCompositeAnnotation returns False. |
| [ContainingOccurrence](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy_Definition.md) | Gets and sets the ModelCompositeAnnotationDefinition associative with this object. |
| [HealthStatus](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy_InternalName.md) | Gets the internal name (GUID) of the model annotation. |
| [IsMemberOfCompositeAnnotation](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy_IsMemberOfCompositeAnnotation.md) | Returns whether this annotation is a member of a ModelCompositeAnnotation. |
| [IsOwnedByToleranceFeature](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy_IsOwnedByToleranceFeature.md) | Returns whether this annotation is owned by a ModelToleranceFeature. |
| [Name](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy_Name.md) | Read-write property that gets and sets the name of the annotation. |
| [NativeObject](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedByToleranceFeature](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy_OwnedByToleranceFeature.md) | Returns the owning ModelToleranceFeature object. |
| [Parent](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy_Parent.md) | Read-only property that returns the parent component definition of the object. |
| [TopToleranceFeature](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy_TopToleranceFeature.md) | Returns the top ModelToleranceFeature object. |
| [Type](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../ModelCompositeAnnotationProxy/ModelCompositeAnnotationProxy_Visible.md) | Gets and sets the visibility of the annotation. |

## Version

Introduced in version 2018
