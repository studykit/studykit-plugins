# Balloons.Add Method

Parent Object: [Balloons](../Balloons/Balloons.md)

## Description

Method that creates a new Balloon. The newly created Balloon is returned. The corresponding BOMView in the model is automatically enabled if not already enabled.

## Syntax

Balloons.**Add**( ***LeaderPoints*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), [***VirtualComponent***] As Variant, [***Level***] As Variant, [***NumberingScheme***] As Variant, [***BalloonStyle***] As Variant, [***Layer***] As Variant ) As [Balloon](../Balloon/Balloon.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| LeaderPoints | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection containing a series of Point2d objects representing the leader originating at the note. The last item in the collection (even if it is the only item) must be a GeometryIntent object indicating a geometry to attach the leader to. A GeometryIntent object can be created using the Sheet.CreateGeometryIntent method. The ObjectCollection must contain at least one item (a GeometryIntent), else the method will fail. Note that the component that the balloon will attach to is inferred from the GeometryIntent object. |
| VirtualComponent | Variant | Optional input object that defines the virtual or custom component that this balloon will be attached to. This can either be a ComponentOccurrence / ComponentOccurrenceProxy object representing a virtual component, a BOMRow that represents a virtual component or a custom/virtual DrawingBOMRow. |
| Level | Variant | Optional input PartsListLevelEnum that sets the view type for the parts list. If supplied, this input is only used in the case where the balloon references an assembly document. If this value was previously set as a result of creating a parts list or a balloon in the drawing based on the same model, this argument is ignored. Use the DrawingDocument.DrawingBOMs.IsDrawingBOMDefined method to check whether or not to supply this argument. Valid enums are: kStructured, that creates a 'first level only' parts list in which a simple integer value is assigned to direct children, kStructuredAllLevels that creates an 'all level' parts list with full expanded numbering, and kPartsOnly, that creates a parts list that sequentially numbers all parts in the top level assembly, even if they are contained in subassemblies.   This is an optional argument whose default value is null. |
| NumberingScheme | Variant | Optional input NameValueMap object that specifies the numbering scheme to use for the parts list. This argument is ignored if the numbering schemes have already been set for this model as a result of creating a parts list or a balloon based on the same model. Use the DrawingDocument.DrawingBOMs.IsDrawingBOMDefined method to check whether or not to supply this argument. Also, this argument is ignored if the numbering schemes have been defined in the model BOM views. The NameValueMap can contain the following entries based on the input 'Level' argument:  For kStructured: 'MinimumDigits' As Long  For kStructuredAllLevels: 'Delimiter' As String  For kPartsOnly: 'NumberingScheme' As NumberingSchemeEnum and 'MinimumDigits' As Long  Valid values for NumberingSchemeEnum are kNumericNumbering, kLowercaseAlphaNumbering and kUppercaseAlphaNumbering. This input should be supplied only if the input argument Level is specified to be kPartsOnly. If this argument is not supplied for a 'parts only' parts list, a default value of kNumericNumbering is assumed.    This is an optional argument whose default value is null. |
| BalloonStyle | Variant | Optional input BalloonStyle object that specifies the balloon style to use for the balloon. If not specified, the style defined by the active standard is used.     This is an optional argument whose default value is null. |
| Layer | Variant | Optional input Layer object that specifies the layer to use for the balloon. If not specified, the layer defined by the active standard is used.   This is an optional argument whose default value is null. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creation a balloon](../../sample-programs/Balloons_Add_Sample.md) | This sample demonstrates the creation of a balloon. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |