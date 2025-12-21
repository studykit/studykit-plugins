# ModelSurfaceTextureSymbol Object

Derived from: [ModelAnnotation](../ModelAnnotation/ModelAnnotation.md) Object

## Description

ModelSurfaceTextureSymbol Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ModelSurfaceTextureSymbol/ModelSurfaceTextureSymbol_Delete.md) | Method that deletes the ModelDimension. |
| [GetDisplayGeometry](../ModelSurfaceTextureSymbol/ModelSurfaceTextureSymbol_GetDisplayGeometry.md) | Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids. |
| [GetFilledAreaFacetsInfo](../ModelSurfaceTextureSymbol/ModelSurfaceTextureSymbol_GetFilledAreaFacetsInfo.md) | Returns facets’ coordinates of the filled areas of the annotation. |
| [GetReferenceKey](../ModelSurfaceTextureSymbol/ModelSurfaceTextureSymbol_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelSurfaceTextureSymbol/ModelSurfaceTextureSymbol_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../ModelSurfaceTextureSymbol/ModelSurfaceTextureSymbol_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CompositeAnnotation](../ModelSurfaceTextureSymbol/ModelSurfaceTextureSymbol_CompositeAnnotation.md) | Read-only property that returns the ModelCompositeAnnotation object if this annotation is a member of it. This returns Nothing if the IsMemberOfCompositeAnnotation returns False. |
| [Definition](../ModelSurfaceTextureSymbol/ModelSurfaceTextureSymbol_Definition.md) | Read-write property that gets and sets the definition associated with this symbol. When reading this property, the definition returned remains associated to the dimension and any changes made to the definition will be immediately reflected in the dimension.To. |
| [HealthStatus](../ModelSurfaceTextureSymbol/ModelSurfaceTextureSymbol_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../ModelSurfaceTextureSymbol/ModelSurfaceTextureSymbol_InternalName.md) | Gets the internal name (GUID) of the model annotation. |
| [IsMemberOfCompositeAnnotation](../ModelSurfaceTextureSymbol/ModelSurfaceTextureSymbol_IsMemberOfCompositeAnnotation.md) | Returns whether this annotation is a member of a ModelCompositeAnnotation. |
| [IsOwnedByToleranceFeature](../ModelSurfaceTextureSymbol/ModelSurfaceTextureSymbol_IsOwnedByToleranceFeature.md) | Returns whether this annotation is owned by a ModelToleranceFeature. |
| [Name](../ModelSurfaceTextureSymbol/ModelSurfaceTextureSymbol_Name.md) | Read-write property that gets and sets the name of the annotation. |
| [OwnedByToleranceFeature](../ModelSurfaceTextureSymbol/ModelSurfaceTextureSymbol_OwnedByToleranceFeature.md) | Returns the owning ModelToleranceFeature object. |
| [Parent](../ModelSurfaceTextureSymbol/ModelSurfaceTextureSymbol_Parent.md) | Read-only property that returns the parent component definition of the object. |
| [TopToleranceFeature](../ModelSurfaceTextureSymbol/ModelSurfaceTextureSymbol_TopToleranceFeature.md) | Returns the top ModelToleranceFeature object. |
| [Type](../ModelSurfaceTextureSymbol/ModelSurfaceTextureSymbol_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../ModelSurfaceTextureSymbol/ModelSurfaceTextureSymbol_Visible.md) | Gets and sets the visibility of the annotation. |

## Accessed From

[ModelSurfaceTextureSymbolDefinition.Parent](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_Parent.md), [ModelSurfaceTextureSymbolProxy.NativeObject](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy_NativeObject.md), [ModelSurfaceTextureSymbols.Add](../ModelSurfaceTextureSymbols/ModelSurfaceTextureSymbols_Add.md), [ModelSurfaceTextureSymbols.Item](../ModelSurfaceTextureSymbols/ModelSurfaceTextureSymbols_Item.md)

## Derived Classes

[ModelSurfaceTextureSymbolProxy](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy.md)

## Version

Introduced in version 2018
