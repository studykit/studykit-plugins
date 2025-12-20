# ModelWeldingSymbolProxy Object

Derived from: [ModelWeldingSymbol](../ModelWeldingSymbol/ModelWeldingSymbol.md) Object

## Description

ModelWeldingSymbolProxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy_Delete.md) | Method that deletes the ModelDimension. |
| [GetDisplayGeometry](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy_GetDisplayGeometry.md) | Method that returns simple linear geometry that represents the display geometry of the annotation. The result is returned as groups of connected lines (polylines). Groups can optionally be filled with internal voids. |
| [GetFilledAreaFacetsInfo](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy_GetFilledAreaFacetsInfo.md) | Returns facets’ coordinates of the filled areas of the annotation. |
| [GetReferenceKey](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AttributeSets](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CompositeAnnotation](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy_CompositeAnnotation.md) | Read-only property that returns the ModelCompositeAnnotation object if this annotation is a member of it. This returns Nothing if the IsMemberOfCompositeAnnotation returns False. |
| [ContainingOccurrence](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy_ContainingOccurrence.md) | Use F1 key to display help topic. |
| [Definitions](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy_Definitions.md) | Gets and sets the ModelWeldingSymbolDefinitions object associated with this symbol. |
| [HealthStatus](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InternalName](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy_InternalName.md) | Gets the internal name (GUID) of the model annotation. |
| [IsMemberOfCompositeAnnotation](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy_IsMemberOfCompositeAnnotation.md) | Returns whether this annotation is a member of a ModelCompositeAnnotation. |
| [IsOwnedByToleranceFeature](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy_IsOwnedByToleranceFeature.md) | Returns whether this annotation is owned by a ModelToleranceFeature. |
| [Name](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy_Name.md) | Read-write property that gets and sets the name of the annotation. |
| [NativeObject](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy_NativeObject.md) | Use F1 key to display help topic. |
| [OwnedByToleranceFeature](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy_OwnedByToleranceFeature.md) | Returns the owning ModelToleranceFeature object. |
| [Parent](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy_Parent.md) | Read-only property that returns the parent component definition of the object. |
| [TopToleranceFeature](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy_TopToleranceFeature.md) | Returns the top ModelToleranceFeature object. |
| [Type](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy_Visible.md) | Gets and sets the visibility of the annotation. |

## Version

Introduced in version 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |