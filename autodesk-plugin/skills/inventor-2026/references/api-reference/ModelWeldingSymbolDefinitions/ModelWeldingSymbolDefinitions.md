# ModelWeldingSymbolDefinitions Object

## Description

The ModelWeldingSymbolDefinitions collection object provides access to the definitions for a model welding symbol and provides methods to create additional ones.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Add](../ModelWeldingSymbolDefinitions/ModelWeldingSymbolDefinitions_Add.md) | Method that creates a new ModelWeldingSymbolDefinition. |
| [AddFromWeldBead](../ModelWeldingSymbolDefinitions/ModelWeldingSymbolDefinitions_AddFromWeldBead.md) | Method that creates a new ModelWeldingSymbolDefinition. The new ModelWeldingSymbolDefinition will extract info from the WeldBead object but no associative with it so users can then modify the properties if necessary. |
| [Copy](../ModelWeldingSymbolDefinitions/ModelWeldingSymbolDefinitions_Copy.md) | Method that creates a copy of this ModelWeldingSymbolDefinitions object. The new ModelWeldingSymbolDefinitions object is independent of any model welding symbol. It can be edited and used as input to edit an existing model welding symbol or to create a new m. |
| [Remove](../ModelWeldingSymbolDefinitions/ModelWeldingSymbolDefinitions_Remove.md) | Method that removes the specified ModelWeldingSymbolDefinition from the ModelWeldingSymbolDefinitions collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AnnotationPlane](../ModelWeldingSymbolDefinitions/ModelWeldingSymbolDefinitions_AnnotationPlane.md) | Gets and sets the annotation plane for the welding symbol. |
| [AnnotationPlaneDefinition](../ModelWeldingSymbolDefinitions/ModelWeldingSymbolDefinitions_AnnotationPlaneDefinition.md) | Gets and sets the annotation plane definition for the symbol. |
| [Application](../ModelWeldingSymbolDefinitions/ModelWeldingSymbolDefinitions_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AssociatedGeometries](../ModelWeldingSymbolDefinitions/ModelWeldingSymbolDefinitions_AssociatedGeometries.md) | Gets and sets the associated geometries. Valid geometries include faces, edges and vertices. |
| [Count](../ModelWeldingSymbolDefinitions/ModelWeldingSymbolDefinitions_Count.md) | Gets the number of items in this collection. |
| [Intent](../ModelWeldingSymbolDefinitions/ModelWeldingSymbolDefinitions_Intent.md) | Gets and sets the geometric entity the welding symbol is attached to. |
| [Item](../ModelWeldingSymbolDefinitions/ModelWeldingSymbolDefinitions_Item.md) | Allows integer-indexed access to items in the collection. |
| [Leader](../ModelWeldingSymbolDefinitions/ModelWeldingSymbolDefinitions_Leader.md) | Read-only property that returns the leader associated with the model welding symbol. |
| [Position](../ModelWeldingSymbolDefinitions/ModelWeldingSymbolDefinitions_Position.md) | Gets and sets the position of the welding symbol in the part or assembly. The point is projected onto the orientation plane. |
| [Type](../ModelWeldingSymbolDefinitions/ModelWeldingSymbolDefinitions_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[ModelWeldingSymbol.Definitions](../ModelWeldingSymbol/ModelWeldingSymbol_Definitions.md), [ModelWeldingSymbolDefinitions.Copy](../ModelWeldingSymbolDefinitions/ModelWeldingSymbolDefinitions_Copy.md), [ModelWeldingSymbolProxy.Definitions](../ModelWeldingSymbolProxy/ModelWeldingSymbolProxy_Definitions.md), [ModelWeldingSymbols.CreateDefinitions](../ModelWeldingSymbols/ModelWeldingSymbols_CreateDefinitions.md)

## Version

Introduced in version 2024
