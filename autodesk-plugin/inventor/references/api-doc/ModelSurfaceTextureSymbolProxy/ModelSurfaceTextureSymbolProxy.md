# ModelSurfaceTextureSymbolProxy Object

Derived from: [ModelSurfaceTextureSymbol](../ModelSurfaceTextureSymbol/ModelSurfaceTextureSymbol.md) Object

## Description

ModelSurfaceTextureSymbolProxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy_Delete.md) | Method that deletes the ModelDimension. |
| [GetDisplayGeometry](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy_GetDisplayGeometry.md) | Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids. |
| [GetFilledAreaFacetsInfo](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy_GetFilledAreaFacetsInfo.md) | Returns facets’ coordinates of the filled areas of the annotation. |
| [GetReferenceKey](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CompositeAnnotation](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy_CompositeAnnotation.md) | Read-only property that returns the ModelCompositeAnnotation object if this annotation is a member of it. This returns Nothing if the IsMemberOfCompositeAnnotation returns False. |
| [ContainingOccurrence](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy_Definition.md) | Read-write property that gets and sets the definition associated with this symbol. When reading this property, the definition returned remains associated to the dimension and any changes made to the definition will be immediately reflected in the dimension.To. |
| [HealthStatus](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy_InternalName.md) | Gets the internal name (GUID) of the model annotation. |
| [IsMemberOfCompositeAnnotation](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy_IsMemberOfCompositeAnnotation.md) | Returns whether this annotation is a member of a ModelCompositeAnnotation. |
| [IsOwnedByToleranceFeature](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy_IsOwnedByToleranceFeature.md) | Returns whether this annotation is owned by a ModelToleranceFeature. |
| [Name](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy_Name.md) | Read-write property that gets and sets the name of the annotation. |
| [NativeObject](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedByToleranceFeature](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy_OwnedByToleranceFeature.md) | Returns the owning ModelToleranceFeature object. |
| [Parent](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy_Parent.md) | Read-only property that returns the parent component definition of the object. |
| [TopToleranceFeature](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy_TopToleranceFeature.md) | Returns the top ModelToleranceFeature object. |
| [Type](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy_Visible.md) | Gets and sets the visibility of the annotation. |

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |