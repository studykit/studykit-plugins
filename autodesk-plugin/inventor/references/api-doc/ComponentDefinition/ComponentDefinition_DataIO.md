# ComponentDefinition.DataIO Property

Parent Object: [ComponentDefinition](../ComponentDefinition/ComponentDefinition.md)

## Description

Gets the object that directly deals with I/O to and from a storage-medium, including Streams(IStream).

## Syntax

ComponentDefinition.**DataIO**() As [DataIO](../DataIO/DataIO.md)

## Property Value

This is a read only property whose value is a [DataIO](../DataIO/DataIO.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Translate - Sheet Metal to DXF](../../sample-programs/WriteFlatPatternAsDXF_Sample.md) | The sample code below writes a sheet metal file out as DXF. DWG is also supported. Use either the FLAT PATTERN DWG or FLAT PATTERN DXF formats.There are several optional arguments that can be specified as part of the format string. E.g. 'FLAT PATTERN DXF?TangentLayer=Tangents&SimplifySplines=True'). Below are the names of these arguments and relevant default values. The output will use these values unless you override them as part of the input string.  |  |  |  |  | | --- | --- | --- | --- | | **Argument** | **Type** | **Default Value** | **Note** | | TangentLayer | String | IV\_TANGENT |  | | OuterProfileLayer | String | IV\_OUTER\_PROFILE |  | | ArcCentersLayer | String | IV\_ARC\_CENTERS |  | | InteriorProfilesLayer | String | IV\_INTERIOR\_PROFILES |  | | BendLayer | String | IV\_BEND | BendUpLayer + BendDownLayer (legacy support) | | BendUpLayer | String | IV\_BEND |  | | BendDownLayer | String | IV\_BEND\_DOWN |  | | ToolCenterLayer | String | IV\_TOOL\_CENTER | ToolCenterUpLayer + ToolCenterDownLayer (legacy support) | | ToolCenterUpLayer | String | IV\_TOOL\_CENTER |  | | ToolCenterDownLayer | String | IV\_TOOL\_CENTER\_DOWN |  | | FeatureProfilesLayer | String | IV\_FEATURE\_PROFILES | FeatureProfilesUpLayer + FeatureProfilesDownLayer (legacy support) | | FeatureProfilesUpLayer | String | IV\_FEATURE\_PROFILES |  | | FeatureProfilesDownLayer | String | IV\_FEATURE\_PROFILES\_DOWN |  | | AltRepFrontLayer | String | IV\_ALTREP\_FRONT |  | | AltRepBackLayer | String | IV\_ALTREP\_BACK |  | | UnconsumedSketchesLayer | String | IV\_UNCONSUMED\_SKETCHES |  | | UnconsumedSketchConstructionLayer | String | IV\_UNCONSUMED\_SKETCH\_CONSTRUCTION |  | | TangentRollLinesLayer | String | IV\_ROLL\_TANGENT |  | | RollLinesLayer | String | IV\_ROLL |  | | \*\*\*Color | String |  | \*\*\* indicates name of layer from the argument column. RGB values separated by ;. Example: TangentLayerColor=255;0;0 | | \*\*\*LineType | Long |  | \*\*\* indicates name of layer from the argument column. Long value from LineTypeEnum. Example: TangentLayerLineType=37644 | | \*\*\*LineWeight | Double |  | \*\*\* indicates name of layer from the argument column. Value in centimeters. Example: TangentLayerLineWeight=.1016 | | CustomizeFilename | String |  |  | | AcadVersion | String |  | 2018, 2013, 2010, 2007, 2004, 2000, or R12 (for DXF only) | | SimplifySplines | Boolean | True | Enable spline replacement(by linear segments or arcs). | | SplineTolerance | Double | 0.01 | Chord tolerance for spline replacement | | AdvancedLegacyExport | Boolean | True |  | | MergeProfilesIntoPolyline | Boolean | False | Build a polyline of the exterior profiles | | RebaseGeometry | Boolean | False | Move geometry to 1st quadrant | | InvisibleLayers | String |  | List of layer names to make invisible, separated by ; | | TrimCenterlinesAtContour | Boolean | False | Trim the centerlines at contour. | | SimplifyAsTangentArcs | Boolean | False | True: Replace splines by tangent arcs. False: Replace splines by line segments. The SimplifySplines should be specified to True otherwise this option is ignored. | |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |