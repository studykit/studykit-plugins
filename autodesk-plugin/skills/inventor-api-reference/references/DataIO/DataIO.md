# DataIO Object

## Description

Generic object that handles input and output of formatted data. IDataObject-style functionality that's IDispatch-compatible and simplified.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [GetInputFormats](../DataIO/DataIO_GetInputFormats.md) | Obtains all the formats that can be accepted, paired with the storage-mediums on which they can possibly be received. |
| [GetOutputFormats](../DataIO/DataIO_GetOutputFormats.md) | Obtains all the formats that can be output, paired with the storage-mediums into which they can possibly be presented. |
| [ReadDataFromFile](../DataIO/DataIO_ReadDataFromFile.md) | Reads in the specifically formatted contents of a file into the supporting object. |
| [ReadDataFromStream](../DataIO/DataIO_ReadDataFromStream.md) | Reads in the specifically formatted contents of a Stream (IStream) into the supporting object. |
| [WriteDataToFile](../DataIO/DataIO_WriteDataToFile.md) | Writes out the contents of the supporting object in the specified format onto a file. |
| [WriteDataToStream](../DataIO/DataIO_WriteDataToStream.md) | Writes out the contents of the supporting object in the specified format onto a Stream (IStream). If once-dereferenced Stream pointer is NULL, then a Stream is allocated and must be 'Release-d()' by caller. |

## Accessed From

[AssemblyComponentDefinition.DataIO](../AssemblyComponentDefinition/AssemblyComponentDefinition_DataIO.md), [AttributeSet.DataIO](../AttributeSet/AttributeSet_DataIO.md), [AttributeSets.DataIO](../AttributeSets/AttributeSets_DataIO.md), [ComponentDefinition.DataIO](../ComponentDefinition/ComponentDefinition_DataIO.md), [DetailDrawingView.DataIO](../DetailDrawingView/DetailDrawingView_DataIO.md), [DrawingSketch.DataIO](../DrawingSketch/DrawingSketch_DataIO.md), [DrawingView.DataIO](../DrawingView/DrawingView_DataIO.md), [FlatPattern.DataIO](../FlatPattern/FlatPattern_DataIO.md), [PartComponentDefinition.DataIO](../PartComponentDefinition/PartComponentDefinition_DataIO.md), [PlanarSketch.DataIO](../PlanarSketch/PlanarSketch_DataIO.md), [PlanarSketchProxy.DataIO](../PlanarSketchProxy/PlanarSketchProxy_DataIO.md), [SectionDrawingView.DataIO](../SectionDrawingView/SectionDrawingView_DataIO.md), [Sheet.DataIO](../Sheet/Sheet_DataIO.md), [SheetMetalComponentDefinition.DataIO](../SheetMetalComponentDefinition/SheetMetalComponentDefinition_DataIO.md), [Sketch.DataIO](../Sketch/Sketch_DataIO.md), [SketchBlockDefinition.DataIO](../SketchBlockDefinition/SketchBlockDefinition_DataIO.md), [SketchBlockDefinitionProxy.DataIO](../SketchBlockDefinitionProxy/SketchBlockDefinitionProxy_DataIO.md), [SurfaceBody.DataIO](../SurfaceBody/SurfaceBody_DataIO.md), [SurfaceBodyProxy.DataIO](../SurfaceBodyProxy/SurfaceBodyProxy_DataIO.md), [VirtualComponentDefinition.DataIO](../VirtualComponentDefinition/VirtualComponentDefinition_DataIO.md), [WeldmentComponentDefinition.DataIO](../WeldmentComponentDefinition/WeldmentComponentDefinition_DataIO.md), [WeldsComponentDefinition.DataIO](../WeldsComponentDefinition/WeldsComponentDefinition_DataIO.md)

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