# Translator Options

The tables below list the valid name-value pairs that can be used to define the
various options when translating files using the translator add-ins. The serve as
the API equivalent to the Options dialog when translating a file interactively.

Questions about what most of the options do can be answered by reading the Inventor
online help for the thranslator and by experimenting interactively with the various
options in the Options dialog of the "Save Copy As" or "Open" dialogs.

### Import options for Alias, CATIA V4, CATIA V5, IGES, JT, NX, Parasolid, Pro/ENGINEER, Rhino, STL, SAT, STEP, SolidWorks, Fusion and OBJ.

|  |  |  |  |
| --- | --- | --- | --- |
| Option Name | Value Type | Default Value | Supported Translators |
| SaveComponentDuringLoad | Boolean | False | Alias, CATIA V4, CATIA V5, IGES, JT, NX, Parasolid, Pro/ENGINEER, Rhino, STL, STEP, SolidWorks, OBJ |
| SaveLocationIndex | Integer | 0 (Save in workspace) | Alias, CATIA V4, CATIA V5, IGES, JT, NX, Parasolid, Pro/ENGINEER, Rhino, STL, SAT, STEP, SolidWorks , OBJ |
| ComponentDestFolder | String |  | Alias, CATIA V4, CATIA V5, IGES, JT, NX, Parasolid, Pro/ENGINEER, Rhino, STL, SAT, STEP, SolidWorks , OBJ |
| SaveAssemSeperateFolder | Boolean | False | Alias, CATIA V4, CATIA V5, IGES, JT, NX, Parasolid, Pro/ENGINEER, SAT, STEP, SolidWorks |
| AssemDestFolder | String |  | Alias, CATIA V4, CATIA V5, IGES, JT, NX, Parasolid, Pro/ENGINEER, SAT, STEP, SolidWorks, Fusion |
| EmbedInDocument | Boolean | True | Alias, CATIA V4, CATIA V5, IGES, JT, NX, Parasolid, Pro/ENGINEER, Rhino, STL, STEP, SolidWorks , OBJ |
| SaveToDisk | Boolean | False | Alias, CATIA V4, CATIA V5, IGES, JT, NX, Parasolid, Pro/ENGINEER, Rhino, STL, STEP, SolidWorks , OBJ |
| ImportSolid | Boolean | True | Alias, CATIA V4, CATIA V5, IGES, JT, NX, Parasolid, Pro/ENGINEER, Rhino, STEP, SolidWorks, Fusion |
| ImportSurface | Boolean | True | Alias, CATIA V4, CATIA V5, IGES, JT, NX, Parasolid, Pro/ENGINEER, Rhino, STEP, SolidWorks, Fusion |
| ImportWire | Boolean | True | Alias, CATIA V4, CATIA V5, IGES, JT, NX, Parasolid, Pro/ENGINEER, Rhino, STEP, SolidWorks, Fusion |
| ImportWorkPlane | Boolean | True | JT, NX, Pro/ENGINEER |
| ImportWorkAxe | Boolean | True | JT, NX, Pro/ENGINEER |
| ImportWorkPoint | Boolean | True | JT, NX, Pro/ENGINEER |
| ImportPoint | Boolean | True | Alias, CATIA V4, CATIA V5, IGES, JT, NX, Parasolid, Rhino, STEP |
| ImportMeshes | Boolean | True | CATIA V4, CATIA V5, Alias, NX, STEP, Rhino, Fusion |
| ImportMeshes | Boolean | False | JT |
| ImportGraphicalPMI | Boolean | True | JT |
| CreateIFO | Boolean | False | Alias, CATIA V4, CATIA V5, IGES, JT, NX, Parasolid, Pro/ENGINEER, Rhino, STEP, SolidWorks, Fusion |
| ImportAASP | Boolean | False | CATIA V4, CATIA V5, IGES, JT, NX, Parasolid, Pro/ENGINEER, SAT, STEP, SolidWorks, Fusion |
| ImportAASPIndex | Integer | 0 (Part with multiple solids) | CATIA V4, CATIA V5, IGES, JT, NX, Parasolid, Pro/ENGINEER, SAT, STEP, SolidWorks, Fusion |
| CreateSurfIndex | Integer | 1 (Single composite) | CATIA V4, CATIA V5, IGES, JT, NX, Parasolid, Pro/ENGINEER, Rhino, SAT, STEP, SolidWorks, Fusion |
| GroupNameIndex | Integer | 0 (Default) | CATIA V4, CATIA V5, IGES, JT, NX, Parasolid, Pro/ENGINEER, Rhino, SAT, STEP, SolidWorks, Fusion |
| GroupName | Integer | 0 | CATIA V4, CATIA V5, IGES, JT, NX, Parasolid, Pro/ENGINEER, Rhino, SAT, STEP, SolidWorks, Fusion |
| ExplodeMSB2Assm | Boolean | True | SAT |
| CHKSearchFolder | Boolean | False | NX |
| SearchFolder | String Array |  | NX |
| AssociativeImport | Boolean | True | Alias, Catia, NX, Pro/ENGINEER, STEP, SolidWorks, Fusion |
| DefaultNames | Boolean | True | SAT |
| CEGroupLevel | Integer | 0 (Level) | IGES, Rhino |
| CEPrefixCk | Boolean | False | Alias, IGES, Rhino, STEP |
| ImportUnit | Integer | 0 (Source unit)   STL, OBJ: 0 (Template units) | CATIA V4, CATIA V5, IGES, JT, NX, Parasolid, Pro/ENGINEER, Rhino, SAT, STEP, SolidWorks, STL, OBJ |
| CheckDuringLoad | Boolean | False | CATIA V4, CATIA V5, IGES, JT, NX, Parasolid, Pro/ENGINEER, Rhino, SAT, STEP, SolidWorks |
| AutoStitchAndPromote | Boolean | True | CATIA V4, CATIA V5, IGES, JT, NX, Parasolid, Pro/ENGINEER, Rhino, SAT, STEP, SolidWorks |
| AdvanceHealing | Boolean | False | CATIA V4, CATIA V5, IGES, JT, NX, Parasolid, Pro/ENGINEER, Rhino, SAT, STEP, SolidWorks |
| NoShowExpModelList (Input) | Boolean | True | CATIA V4 (For \*.exp and \*.div3 import) |
| ExpModelIndex (Input) | Integer | N/A | CATIA V4 (For \*.exp and \*.div3 import) |
| ExpModelCount (Output) | Integer | N/A | CATIA V4 (For \*.exp and \*.div3 import) |
| ExpModelNameList (Output) | String Array | N/A | CATIA V4 (For \*.exp and \*.div3 import) |
| ImportColor | Boolean | True | STL |
| ImportColorIndex | Integer | 0 | STL |
| TessellationDetailIndex | Integer | 0 | JT |
| SplitGroup | Boolean | True | OBJ |
| SaveInSubFolder | Boolean | True | CATIA V4, CATIA V5, IGES, JT, NX, Parasolid, Pro/ENGINEER, Rhino, SAT, SMT, STEP, SolidWorks, Fusion |

### Import options for DWG import when importing into a sketch.

For other DWG import cases, an .ini file is used to define the options. You can manually use the dwg translator to set the various options you want and then write out an .ini file with the settings that you can then specify later when translating via the API.

|  |  |  |  |
| --- | --- | --- | --- |
| Option Name | Value Type | Default Value | Notes |
| ImportModelSpace | Boolean | True | Specifies whether to import model space or not, set this to False to import the layout paper space where you specify the layout name using the SelectedLayout setting. |
| SelectedLayout | String |  | Specifies the layout name to import when the ImportModelSpace setting is set to False. |
| FileUnits | String |  | Specifies the units for import. The units can be “Meters”, ”Feet”, “Microns”, “Inches”, “Centimeters”, or “Millimeters”. If not specified it will use the units from the document. |
| SelectedLayers | String |  | Specifies the layer names to import. The names are comma delimited. |
| InvertLayersSelection | Boolean | True | Specifies whether to invert the layers selection during import. Leaving the SelectedLayers empty and setting this value to True will import all the layers. |
| ConstrainEndPoints | Boolean | False | Specifies if end points constraints should be applied to the imported geometry. |
| ApplyGeometricConstraints | Boolean | False | Specifies if geometric constraints should be applied to the imported geometry to fully constrain the sketch. This is ignored if the ConstrainEndPoints setting is set to False. |
| ImportParametricConstraints | Boolean | False | Specifies if AutoCAD 2D parametric constraints should be imported. |
| ProxyObjectsToUserDefinedSymbols | Boolean | False | Specifies if proxy objects should be converted to user-defined symbols. This is only valid in Inventor drawings. |

### Definitions of Import Values

|  |  |
| --- | --- |
| Option Name | Valid Values |
| SaveLocationIndex | SAVE\_IN\_WORKSPACE = 0  SELECT\_SAVE\_LOCATIONS = 1  SAVE\_AT\_IMPORT\_LOCATION = 2 |
| CreateIFO | 1. When CreateIFO is true, CreateSurfIndex only supports SINGLE\_COMPOSITE or MULTIPLE\_COMPOSITE; if CreateSurfIndex’s value is illegal, it will be set as SINGLE\_COMPOSITE.  2. When CreateIFO is true, AutoStitchAndPromote can be set as true or false.  3. When CreateIFO is true, AdvanceHealing will be set as false. |
| ImportAASPIndex | MULTIPLE\_SOLID\_PART = 0  SINGLE\_COMPOSITE\_FEATURE = 1 |
| CreateSurfIndex | INDIVIDUAL\_SURFACE = 0 (Translates all surfaces to individual ones, and consumes much more memory and time.)  SINGLE\_COMPOSITE = 1  MULTI\_COMPOSITE = 2  SINGLE\_CONSTRUCTION = 3  MULTI\_CONSTRUCTION = 4 |
| GroupNameIndex | DEFAULT = 0  ENTERED\_NAME = 1 |
| CEGroupLevel | eLevelType = 0  eGroupType = 1 |
| ImportUnit | SOURCE\_UNITS = 0  TEMPLATE\_UNITS = 1  INCH = 2  FOOT = 3  CENTIMETER = 4  MILLIMETER = 5  METER = 6  MICRON = 7 |
| NoShowExpModelList | When set to true, a dialog that lists all models in the \*.exp or \*.dlv3 file is shown and ask the user select a file to open. |
| ExpModelIndex | Used for user’s input to open one of the models in the \*.exp or \*.dlv3 file. |
| ExpModelCount | User can get the model count in the \*.exp or \*.dlv3 file. |
| ExpModelNameList | User can get a list of all model"s name in the \*.exp or \*.dlv3 file. |
| ImportColorIndex | RGB = 0  BGR = 1 |
| TessellationDetailIndex | eHighestDetail = 0  eLowestDetail = 1 |

### Export options for CATIA V5, IGES, JT, Parasolid, Pro/ENGINEER, SAT, STEP, STL and OBJ.

|  |  |  |  |
| --- | --- | --- | --- |
| Option Name | Value Type | Default Value | Supported Translators |
| Work Plane Export | Boolean | TRue | JT, Pro/ENGINEER |
| Work Axes Export | Boolean | True | JT |
| Work Point Export | Boolean | True | JT, Pro/ENGINEER |
| IncludeSketches | Boolean | True | CATIA V5, IGES, JT, Parasolid, Pro/ENGINEER, SAT, STEP |
| Version | Integer | CATIA: latest   JT: latest   Pro/ENGINEER Granite: latest   Parasolid: latest   SAT: 7 | CATIA V5, JT, Parasolid, Pro/ENGINEER, SAT |
| ConfigFileEnabled | Boolean | False | JT |
| ConfigFilePath | String |  | JT |
| OutputFileType | Integer | 0 (BrepAndFacets) | JT |
| XTBrep | Boolean | True | JT |
| ExportPMI | Boolean | True | JT |
| FileStructure | Integer | 0 (Monolithic) | JT |
| ApplicationProtocolType | Integer | 4 (eAP214IS) | STEP |
| Author | String |  | STEP |
| Organization | String |  | STEP |
| Authorization | String |  | STEP |
| Description | String |  | STEP |
| GeometryType | Integer | 1 (Solids) | IGES |
| SurfaceType | Integer | 0 (143-Bounded) | IGES |
| SolidFaceType | Integer | 0 (NURBS) | IGES |
| ExportBodyNames | Boolean | False | SAT |
| OutputFileType | Integer | 0 (Binary) | STL |
| ExportUnits | Integer | STL: 4 (Centimeters)   OBJ: 1 (Source unit) | STL, OBJ |
| ExportFileStructure | Integer | 0 (One File) | STL , OBJ |
| Resolution | Integer | 1 (Medium) | STL , OBJ |
| SurfaceDeviation | Integer | 60 | STL , OBJ |
| NormalDeviation | Integer | 14 | STL , OBJ |
| MaxEdgeLength | Integer | 100 | STL , OBJ |
| AspectRatio | Integer | 21.5 | STL , OBJ |
| AllowMoveMeshNode | Boolean | False | STL |
| export\_fit\_tolerance | Double | 0.001 | IGES/STEP |
| ExportColor | Boolean | True | STL |

### Definitions of Export Values

|  |  |
| --- | --- |
| Option Name | Valid Values |
| Version | CATIA V5 (14, 19 - 34) e.g. 34 means "V5-6R2024" version  Pro/Engineer Granite (1 - 16)  JT (80, 81, 82, 90, 91, 92, 93, 94, 95, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109) e.g. 102 means 10.2 version file.  PARASOLID (9 - 36)  SAT (7) |
| OutputFileType | eBrepAndFacets = 0  eBrepOnly = 1  eFacetsOnly = 2 |
| XTBrep | XTBrep = True  JTBrep = False |
| FileStructure | JtkMONOLITHIC = 0  JtkPER\_PART = 1  JtkFULL\_SHATTER =2 |
| ApplicationProtocolType | eAP203 = 2  eAP214IS = 4  eAP242 = 5 |
| GeometryType | SURFACES = 0  SOLIDS = 1  WIREFRAMES = 2 |
| SurfaceType | 143\_Bounded = 0   144\_Trimmed = 1 |
| SolidFaceType | NURBS = 0  ANALYTICS = 1 |
| OutputFileType | BINARY = 0  ASCII = 1 |
| ExportUnits | INCH = 2  FOOT = 3  CENTIMETER = 4  MILLIMETER = 5  METER = 6  MICRON = 7 |
| ExportFileStructure | ONE FILE = 0  ONE FILE PER PART INSTANCE = 1 |
| Resolution | HIGH = 0  MEDIUM = 1  LOW = 2  CUSTOM = 3   BREP = 4 |
| SurfaceDeviation | Range 0 to 100, the value has precision of 0.0001. None-zero value is used if Resolution is CUSTOM (3), otherwise value is ignored. |
| NormalDeviation | Range 0 to 41. Non-zero value is used if Resolution is CUSTOM (3), otherwise value is ignored. Any input value out of this range will be changed to 14 by force. |
| MaxEdgeLength | Range 0 to 100. Non-zero value is used if Resolution is CUSTOM (3), otherwise value is ignored. |
| AspectRatio | Range 0 to 21.5. Non-zero value is used if Resolution is CUSTOM (3), otherwise value is ignored. |
| export\_fit\_tolerance | Set the tolerance for the IGES/STEP file. The accepted range for the tolerance value is from 0.00001 (cm) to 0.001 (cm). You can change this value, using cm units only. A smaller tolerance creates more accurate geometry approximations and larger file size. |
| ExportColor | Write color information to STL binary file. |

---

### Export options for DWF.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Option Name | Value Type | Default Value | Supported Documents | Supported Translators | Notes |
| Launch\_Viewer | Long | 0 | Part, Assembly, Drawing,Presentation | DWF |  |
| Publish\_Mode | DWFPublishModeEnum | kBasicDWFPublish | Part, Assembly, Drawing,Presentation | DWF |  |
| Publish\_Component\_Props | Boolean | False | Part, Assembly, Drawing,Presentation | DWF | Use this to publish ALL component properties |
| Publish\_Mass\_Props | Boolean | False | Part, Assembly, Drawing | DWF | Use this to publish ALL mass properties |
| Publish\_All\_Component\_Props | Boolean | False | Part, Assembly, Drawing,Presentation | DWF | Same as Publish\_Component\_Props |
| Publish\_All\_Physical\_Props | Boolean | False | Part, Assembly, Drawing | DWF | Same as Publish\_Mass\_Props |
| Enable\_Measure | Boolean | True | Part, Assembly, Drawing,Presentation | DWF | DRM protection |
| Enable\_Printing | Boolean | True | Part, Assembly, Drawing,Presentation | DWF | DRM protection |
| Enable\_Markups | Boolean | True | Part, Assembly, Drawing,Presentation | DWF | DRM protection |
| Enable\_Markup\_Edits | Boolean | True | Part, Assembly, Drawing,Presentation | DWF | DRM protection |
| Password | String | "" | Part, Assembly, Drawing,Presentation | DWF |  |
| Password\_Protect | Boolean | False | Part, Assembly, Drawing,Presentation | DWF |  |
| Password\_Type | string or enum |  | Part, Assembly, Drawing,Presentation | DWF |  |
| Enable\_Large\_Assembly\_Mode | Boolean | True | Assembly | DWF | Enables large assembly optimizations (transactions and out of process publishing) |
| Output\_Path | String |  | Part, Assembly, Drawing,Presentation | DWF |  |
| Publish\_3D\_Models | Boolean | False | Drawing | DWF | Specify the publish mode. |
| Publish\_All\_Sheets | Boolean | False | Drawing | DWF |  |
| Include\_Sheet\_Tables | Boolean |  | Drawing | DWF |  |
| Sheet\_Count | Integer |  | Drawing | DWF |  |
| Sheets | NameValueMap |  | Drawing | DWF |  |
| Override\_Sheet\_Color | Boolean | False | Drawing | DWF | Set whether to override the sheet background color. |
| Sheet\_Color | Integer |  | Drawing | DWF | Specify the sheet background color using an Integer. The Integer is calculated with R,G,B values(0 to 255) using below equation:  Sheet\_Color = R+G\*256+B\*65536. |
| Include\_Sheet\_Tables | Boolean | True | Drawing | DWF | Set whether to include sheet tables or not. |
| BOM\_Structured | Boolean | False | Assembly;Presentation | DWF | Set whether to publish the Structured BOM. |
| BOM\_Parts\_Only | Boolean | False | Assembly;Presentation | DWF | Set whether to publish the Parts Only BOM. |
| Design\_Views | NameValueMap |  | Assembly;Presentation | DWF | Specify the design views which will be published. |
| Positional\_Representations | NameValueMap |  | Assembly;Presentation | DWF | Specify the positional representations which will be published. |
| Sheet\_Metal\_Style\_Information | Boolean | False | Sheetmetal | DWF | Specify whether to publish the sheet metal style infomation. |
| Sheet\_Metal\_Flat\_Pattern | Boolean | False | Sheetmetal | DWF | Specify whether to publish the flat pattern. |
| Sheet\_Metal\_Part | Boolean | True | Sheetmetal | DWF | Specify whether to publish the sheet metal part. At least one of the Sheet\_Metal\_Flat\_Pattern and Sheet\_Metal\_Part should be specified as True for a sheet metal publish. |
| Facet\_Quality | AccuracyEnum | kHigh |  | DWF | Specify the facet quality. Only kLow, kMedium and kHigh are valid values for this. |
| Animations | Boolean | False | Presentation | DWF | Specify whether to publish the animations. |
| Instructions | Boolea | False | Presentation | DWF | Specify whether to publish the instructions. This will be ignored if the Animations is set to False. |
| Presentations | NameValueMap |  | Presentation | DWF |  |
| iAssembly\_All\_Members | Boolean | False | iAssembly | DWF | Specify whether to publish all the iAssembly members. |
| iAssembly\_3D\_Models | Boolean | False | iAssembly | DWF | Specify whether to publish all the 3D models for all the iAssembly members. |
| iAssemblies | NameValueMap |  | iAssembly | DWF | Specify which of the iAssembly members will be published. |
| iPart\_All\_Members | Boolean | False | iPart | DWF | Specify whether to publish all the iPart members. |
| iPart\_3D\_Models | Boolean | False | iPart | DWF | Specify whether to publish all the 3D models for all the iPart members. |
| iParts | NameValueMap |  | iPart | DWF | Specify which of the iPart members will be published. |
| Include\_Empty\_Properties | Boolean | False | Part, Assembly, Drawing,Presentation | DWF | Specify whether publish the empty properties |

###

### Definitions of Export Values

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Option Name | Name | Value | Supported Documents | Notes |
| Sheets | Sheet1 | NameValueMap | Drawing | Create a NameValueMap("Sheet1",NameValueMap) to specify options for a sheet, the name should start from Sheet1 and the number increases one by one. |
|  | Sheet2 | NameValueMap | Drawing | See above. |
|  | Sheet# | NameValueMap | Drawing | See above. |
| Sheet1 | Name | String | Drawing | The name of a sheet in drawing, this can be any sheet name but not just for Sheet:1. |
|  | 3DModel | Boolean | Drawing | Specify whether to publish the 3D model for the sheet. |
| Sheet2 | Name | String | Drawing | The name of a sheet in drawing, this can be any sheet name but not just for Sheet:2. |
|  | 3DModel | Boolean | Drawing | Specify whether to publish the 3D model for the sheet. |
| Sheet# | Name | String | Drawing | The name of a sheet in drawing, this can be any sheet name but not just for Sheet:#. |
|  | 3DModel | Boolean | Drawing | Specify whether to publish the 3D model for the sheet. |
| Design\_Views | Design\_View1 | NameValueMap | Assembly | Create a NameValueMap("Design\_View1",NameValueMap) to specify a design view to publish, the name should start from Design\_View1 and the number increases one by one. |
|  | Design\_View2 | NameValueMap | Assembly | See above. |
|  | Design\_View# | NameValueMap | Assembly | See above. |
| Design\_View1 | Name | String | Assembly | The name of a design view. |
| Design\_View2 | Name | String | Assembly | The name of a design view. |
| Design\_View# | Name | String | Assembly | The name of a design view. |
| Positional\_Representations | Positional\_Representation1 | NameValueMap | Assembly | Create a NameValueMap("Positional\_Representation1",NameValueMap) to specify a positional representation to publish, the name should start from Positional\_Representation1 and the number increases one by one. |
|  | Positional\_Representation2 | NameValueMap | Assembly | See above. |
|  | Positional\_Representation1# | NameValueMap | Assembly | See above. |
| Positional\_Representation1 | Name | String | Assembly | The name of a positional representation. |
| Positional\_Representation2 | Name | String | Assembly | The name of a positional representation. |
| Positional\_Representation1# | Name | String | Assembly | The name of a positional representation. |
| Presentations | Presentation1 | NameValueMap | Presentation | Create a NameValueMap("Presentation1",NameValueMap) to specify a presentation view to publish, the name should start from Presentation1 and the number increases one by one. |
|  | Presentation1 | NameValueMap | Presentation | See above. |
|  | Presentation# | NameValueMap | Presentation | See above. |
| Presentation1 | Name | String | Presentation | The name of a presentation explosion view. |
| Presentation2 | Name | String | Presentation | The name of a presentation explosion view. |
| Presentation# | Name | String | Presentation | The name of a presentation explosion view. |
| iAssemblies | Member1 | NameValueMap | iAssembly | Create a NameValueMap("Member1",NameValueMap) to specify options for an iAssembly member, the name should start from Member1 and the number increases one by one. |
|  | Member2 | NameValueMap | iAssembly | See above. |
|  | Member# | NameValueMap | iAssembly | See above. |
| Member1 | Name | String | iAssembly | The name of an iAssembly member, this can be any iAssebly member name. |
|  | 3DModel | Boolean | iAssembly | Specify whether to publish the 3D model for the iAssembly member. |
| Member2 | Name | String | iAssembly | The name of an iAssembly member, this can be any iAssebly member name. |
|  | 3DModel | Boolean | iAssembly | Specify whether to publish the 3D model for the iAssembly member. |
| Member# | Name | String | iAssembly | The name of an iAssembly member, this can be any iAssebly member name. |
|  | 3DModel | Boolean | iAssembly | Specify whether to publish the 3D model for the iAssembly member. |
| iParts | Member1 | NameValueMap | iPart | Create a NameValueMap("Member1",NameValueMap) to specify options for an iPart member, the name should start from Member1 and the number increases one by one. |
|  | Member2 | NameValueMap | iPart | See above. |
|  | Member# | NameValueMap | iPart | See above. |
| Member1 | Name | String | iPart | The name of an iPart member, this can be any iPart member name. |
|  | 3DModel | Boolean | iPart | Specify whether to publish the 3D model for the iPart member. |
| Member2 | Name | String | iPart | The name of an iPart member, this can be any iPart member name. |
|  | 3DModel | Boolean | iPart | Specify whether to publish the 3D model for the iPart member. |
| Member# | Name | String | iPart | The name of an iPart member, this can be any iPart member name. |
|  | 3DModel | Boolean | iPart | Specify whether to publish the 3D model for the iPart member. |

---

### Export options for 3D PDF.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Option Name | Value Type | Default Value | Supported Documents | Supported Translators | Notes |
| AttachedFiles | String array |  | Part, Assembly | 3D PDF | An array of string values indicating the full file paths. |
| ExportAllProperties | Boolean | True | Part, Assembly | 3D PDF | Use this to publish ALL component properties. If set this to False, the ExportProperties can be used to specify which properties to export. |
| ExportDesignViewRepresentations | String array |  | Part, Assembly | 3D PDF | An array of string values indicating the names of the design view representations. |
| ExportProperties | String array |  | Part, Assembly | 3D PDF | A string array that indicates the properties to be exported. Use below format to specify a property to export: “PropertySet.InternalName:Property.Name”. A sample is “{F29F85E0-4FF9-1068-AB91-08002B27B3D9}:Title” which indicates the Title property in “Summary Information” property set. |
| ExportTemplate | String |  | Part, Assembly | 3D PDF | Specify the template PDF full file name. |
| FileOutputLocation | String |  | Part, Assembly | 3D PDF | A string value indicates the PDF full filename to export the document to. |
| GenerateAndAttachSTEPFile | Boolean | False | Part, Assembly | 3D PDF | Specify whether to generate the STEP file and attach it in PDF. |
| LimitToEntitiesInDVRs | Boolean | True | Part, Assembly | 3D PDF | Specify whether the export scope is limited to the selected design view representations. |
| STEPFileOptions | NameValueMap |  | Part, Assembly | 3D PDF | Specify the STEP save options when generate the STEP file. |
| ViewPDFWhenFinished | Boolean | True | Part, Assembly | 3D PDF | Specify whether to view the PDF after the export is finished. |
| VisualizationQuality | AccuracyEnum | kMedium | Part, Assembly | 3D PDF | Specify the visualization quality. |

###

### Definitions of Export Values

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Option Name | Name | Value | Supported Documents | Notes |
| STEPFileOptions | ApplicationProtocolType | Integer value that indicates the application protocol type. Valid values are: eAP203 = 2, eAP214IS = 4 and eAP242 = 5. | Part, Assembly |  |
|  | Author | String value that specifies the author. | Part, Assembly |  |
|  | Authorization | String value that specifies authorization. | Part, Assembly |  |
|  | Description | String value that specifies description. | Part, Assembly |  |
|  | ExportFitTolerance | Double value that specifies export fit tolerance | Part, Assembly |  |
|  | Organization | String value that specifies organization | Part, Assembly |  |
|  | IncludeSketches | Boolean value that specifies whether include sketches or not. | Part, Assembly |  |

---

## STL Export Format

When exporting an STL through the user-interface or using the API, you have an option of whether to include color information. Color information is not part of the STL standard but companies have figured out ways to add color information into the file in ways that allows standard STL readers to continue to be able to read the file and ignore the colors. If you have an STL reader and want to support colors from Inventor STL files you need to understand how the color is encoded within the binary STL file. Color is not supported in STL ASCII files. Inventor uses a format designed by Materialise and is described on [Wikipedia](http://en.wikipedia.org/wiki/STL_format).

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |