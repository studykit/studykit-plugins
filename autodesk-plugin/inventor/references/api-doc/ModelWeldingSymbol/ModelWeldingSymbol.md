# ModelWeldingSymbol Object

Derived from: [ModelAnnotation](../ModelAnnotation/ModelAnnotation.md) Object

## Description

ModelWeldingSymbol Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ModelWeldingSymbol/ModelWeldingSymbol_Delete.md) | Method that deletes the ModelDimension. |
| [GetDisplayGeometry](../ModelWeldingSymbol/ModelWeldingSymbol_GetDisplayGeometry.md) | Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids. |
| [GetFilledAreaFacetsInfo](../ModelWeldingSymbol/ModelWeldingSymbol_GetFilledAreaFacetsInfo.md) | Returns facets’ coordinates of the filled areas of the annotation. |
| [GetReferenceKey](../ModelWeldingSymbol/ModelWeldingSymbol_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelWeldingSymbol/ModelWeldingSymbol_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../ModelWeldingSymbol/ModelWeldingSymbol_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CompositeAnnotation](../ModelWeldingSymbol/ModelWeldingSymbol_CompositeAnnotation.md) | Read-only property that returns the ModelCompositeAnnotation object if this annotation is a member of it. This returns Nothing if the IsMemberOfCompositeAnnotation returns False. |
| [Definitions](../ModelWeldingSymbol/ModelWeldingSymbol_Definitions.md) | Gets and sets the ModelWeldingSymbolDefinitions object associated with this symbol. |
| [HealthStatus](../ModelWeldingSymbol/ModelWeldingSymbol_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../ModelWeldingSymbol/ModelWeldingSymbol_InternalName.md) | Gets the internal name (GUID) of the model annotation. |
| [IsMemberOfCompositeAnnotation](../ModelWeldingSymbol/ModelWeldingSymbol_IsMemberOfCompositeAnnotation.md) | Returns whether this annotation is a member of a ModelCompositeAnnotation. |
| [IsOwnedByToleranceFeature](../ModelWeldingSymbol/ModelWeldingSymbol_IsOwnedByToleranceFeature.md) | Returns whether this annotation is owned by a ModelToleranceFeature. |
| [Name](../ModelWeldingSymbol/ModelWeldingSymbol_Name.md) | Read-write property that gets and sets the name of the annotation. |
| [OwnedByToleranceFeature](../ModelWeldingSymbol/ModelWeldingSymbol_OwnedByToleranceFeature.md) | Returns the owning ModelToleranceFeature object. |
| [Parent](../ModelWeldingSymbol/ModelWeldingSymbol_Parent.md) | Read-only property that returns the parent component definition of the object. |
| [TopToleranceFeature](../ModelWeldingSymbol/ModelWeldingSymbol_TopToleranceFeature.md) | Returns the top ModelToleranceFeature object. |
| [Type](../ModelWeldingSymbol/ModelWeldingSymbol_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../ModelWeldingSymbol/ModelWeldingSymbol_Visible.md) | Gets and sets the visibility of the annotation. |

## Accessed From

[ModelWeldingSymbolDefinition.Parent](../ModelWeldingSymbolDefinition/ModelWeldingSymbolDefinition_Parent.md), [ModelWeldingSymbolProxy.NativeObject](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy_NativeObject.md), [ModelWeldingSymbols.Add](../ModelWeldingSymbols/ModelWeldingSymbols_Add.md), [ModelWeldingSymbols.Item](../ModelWeldingSymbols/ModelWeldingSymbols_Item.md)

## Derived Classes

[ModelWeldingSymbolProxy](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy.md)

## Version

Introduced in version 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |