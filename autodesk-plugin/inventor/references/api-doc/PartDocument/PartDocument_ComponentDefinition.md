# PartDocument.ComponentDefinition Property

Parent Object: [PartDocument](../PartDocument/PartDocument.md)

## Description

Gets the primary ComponentDefinition that resides in this file (housing the BRep and its geometric Feature Constraints).

## Syntax

PartDocument.**ComponentDefinition**() As [PartComponentDefinition](../PartComponentDefinition/PartComponentDefinition.md)

## Property Value

This is a read only property whose value is a [PartComponentDefinition](../PartComponentDefinition/PartComponentDefinition.md).

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Adding iPart occurrences to an assembly](../../sample-programs/AddiPartMember_Sample.md) | This sample demonstrates adding iPart occurrences to an assembly. |
| [Add assembly insert constraint](../../sample-programs/AssemblyConstraints_AddInsertConstraint_Sample.md) | This sample demonstrates the creation of an assembly insert constraint. |
| [Add assembly mate constraint](../../sample-programs/AssemblyConstraints_AddMateConstraint_Sample.md) | This sample demonstrates the creation of an assembly mate constraint. |
| [Delete Face, Boundary Patch and Stitch features](../../sample-programs/BoundaryPatchFeatures_Add_Sample.md) | Demonstrates creating Face, Boundary Patch and Stitch features. |
| [Navigation between browser and data](../../sample-programs/BrowserPanes_GetNativeBrowserNodeDefinition_Sample.md) | This sample demonstrates the navigation between a browser node and it's corresponding data model object and vice versa. This sample creates a work plane, finds its browser node and gets the work plane object back from the browser node. |
| [Client Graphics - Draw Range Box](../../sample-programs/ClientGraphics_Sample.md) | This sample demonstrates the use of client graphics to draw the range box of selected entities. |
| [Assembly Ground Occurrences](../../sample-programs/ComponentOccurrence_Grounded_Sample.md) | This sample demonstrates grounding an assembly occurrence. |
| [Copy a sketch](../../sample-programs/CopySketch_Sample.md) | This sample demonstrates copying the contents of a sketch into another sketch via the API. |
| [Creating a new parameter group](../../sample-programs/CustomParameterGroup_Add_Sample.md) | This sample demonstrates the creation of model, reference and user parameters and copying these parameters to a newly created group. |
| [Create a Configuration Table](../../sample-programs/CustomTables_AddConfigurationTable_Sample.md) | This sample demonstrates the creation of a configuration (iPart/iAssembly) table in a drawing from a factory document. |
| [Add a decal feature](../../sample-programs/DecalFeatures_Add_Sample.md) | This sample demonstrates the creation of a decal feature. |
| [Derived Parts and Assemblies](../../sample-programs/DerivedAssemblyComponents_Add_Sample.md) | This sample demonstrates the use of the API to create derived parts and assemblies. |
| [Selectively link paramaters](../../sample-programs/DerivedParameterTables_Add2_Sample.md) | This sample demonstrates the selective linking of parameters from another Inventor file. |
| [Display feature information](../../sample-programs/DumpFeatureInfo_Sample.md) | Displays information about all of the extrude features in the active document. A part document must be active when this is run. |
| [Extrude Feature - Create Block with Pocket](../../sample-programs/ExtrudeFeature_Sample.md) | This sample demonstrates creating a simple solid consisting a block with a pocket. It shows how to create a sketch plane at a specified orientation to existing geometry. |
| [Hole Feature - Through holes (RegularAndTapped)](../../sample-programs/HoleFeature_Sample.md) | This sample demonstrates the creation of through holes, both regular and tapped. |
| [Table Parameters](../../sample-programs/ParameterTables_Sample.md) | This sample demonstrates how to access the Parameters object, and from it in turn the TableParameters collection that represents the collection of parameters that have been linked/embedded from an external spreadsheet. |
| [Add a punch tool feature](../../sample-programs/PunchToolFeatures_Add_Sample.md) | This program demonstrates the creation of a punch tool feature. It uses one of the punch features that's delivered with Inventor. It assumes you already have an existing sheet metal part and have selected a face to place the punch feature on. The selected face should be large so there is room for the punch features. |
| [Sheet Metal Feature Display](../../sample-programs/SheetMetalComponentDefinition_Sample.md) | This sample illustrates getting basic information from the various sheet metal features. |
| [Translate - Sheet Metal to DXF](../../sample-programs/WriteFlatPatternAsDXF_Sample.md) | The sample code below writes a sheet metal file out as DXF. DWG is also supported. Use either the FLAT PATTERN DWG or FLAT PATTERN DXF formats.There are several optional arguments that can be specified as part of the format string. E.g. 'FLAT PATTERN DXF?TangentLayer=Tangents&SimplifySplines=True'). Below are the names of these arguments and relevant default values. The output will use these values unless you override them as part of the input string.  |  |  |  |  | | --- | --- | --- | --- | | **Argument** | **Type** | **Default Value** | **Note** | | TangentLayer | String | IV\_TANGENT |  | | OuterProfileLayer | String | IV\_OUTER\_PROFILE |  | | ArcCentersLayer | String | IV\_ARC\_CENTERS |  | | InteriorProfilesLayer | String | IV\_INTERIOR\_PROFILES |  | | BendLayer | String | IV\_BEND | BendUpLayer + BendDownLayer (legacy support) | | BendUpLayer | String | IV\_BEND |  | | BendDownLayer | String | IV\_BEND\_DOWN |  | | ToolCenterLayer | String | IV\_TOOL\_CENTER | ToolCenterUpLayer + ToolCenterDownLayer (legacy support) | | ToolCenterUpLayer | String | IV\_TOOL\_CENTER |  | | ToolCenterDownLayer | String | IV\_TOOL\_CENTER\_DOWN |  | | FeatureProfilesLayer | String | IV\_FEATURE\_PROFILES | FeatureProfilesUpLayer + FeatureProfilesDownLayer (legacy support) | | FeatureProfilesUpLayer | String | IV\_FEATURE\_PROFILES |  | | FeatureProfilesDownLayer | String | IV\_FEATURE\_PROFILES\_DOWN |  | | AltRepFrontLayer | String | IV\_ALTREP\_FRONT |  | | AltRepBackLayer | String | IV\_ALTREP\_BACK |  | | UnconsumedSketchesLayer | String | IV\_UNCONSUMED\_SKETCHES |  | | UnconsumedSketchConstructionLayer | String | IV\_UNCONSUMED\_SKETCH\_CONSTRUCTION |  | | TangentRollLinesLayer | String | IV\_ROLL\_TANGENT |  | | RollLinesLayer | String | IV\_ROLL |  | | \*\*\*Color | String |  | \*\*\* indicates name of layer from the argument column. RGB values separated by ;. Example: TangentLayerColor=255;0;0 | | \*\*\*LineType | Long |  | \*\*\* indicates name of layer from the argument column. Long value from LineTypeEnum. Example: TangentLayerLineType=37644 | | \*\*\*LineWeight | Double |  | \*\*\* indicates name of layer from the argument column. Value in centimeters. Example: TangentLayerLineWeight=.1016 | | CustomizeFilename | String |  |  | | AcadVersion | String |  | 2018, 2013, 2010, 2007, 2004, 2000, or R12 (for DXF only) | | SimplifySplines | Boolean | True | Enable spline replacement(by linear segments or arcs). | | SplineTolerance | Double | 0.01 | Chord tolerance for spline replacement | | AdvancedLegacyExport | Boolean | True |  | | MergeProfilesIntoPolyline | Boolean | False | Build a polyline of the exterior profiles | | RebaseGeometry | Boolean | False | Move geometry to 1st quadrant | | InvisibleLayers | String |  | List of layer names to make invisible, separated by ; | | TrimCenterlinesAtContour | Boolean | False | Trim the centerlines at contour. | | SimplifyAsTangentArcs | Boolean | False | True: Replace splines by tangent arcs. False: Replace splines by line segments. The SimplifySplines should be specified to True otherwise this option is ignored. | |

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |