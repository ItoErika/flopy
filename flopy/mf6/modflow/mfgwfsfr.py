# DO NOT MODIFY THIS FILE DIRECTLY.  THIS FILE MUST BE CREATED BY
# mf6/utils/createpackages.py
from .. import mfpackage
from ..data.mfdatautil import ListTemplateGenerator, ArrayTemplateGenerator


class ModflowGwfsfr(mfpackage.MFPackage):
    """
    ModflowGwfsfr defines a sfr package within a gwf6 model.

    Parameters
    ----------
    auxiliary : [string]
        * auxiliary (string) defines an array of one or more auxiliary variable
          names. There is no limit on the number of auxiliary variables that
          can be provided on this line; however, lists of information provided
          in subsequent blocks must have a column of data for each auxiliary
          variable name defined here. The number of auxiliary variables
          detected on this line determines the value for naux. Comments cannot
          be provided anywhere on this line as they will be interpreted as
          auxiliary variable names. Auxiliary variables may not be used by the
          package, but they will be available for use by other parts of the
          program. The program will terminate with an error if auxiliary
          variables are specified on more than one line in the options block.
    boundnames : boolean
        * boundnames (boolean) keyword to indicate that boundary names may be
          provided with the list of stream reach cells.
    print_input : boolean
        * print_input (boolean) keyword to indicate that the list of stream
          reach information will be written to the listing file immediately
          after it is read.
    print_stage : boolean
        * print_stage (boolean) keyword to indicate that the list of stream
          reach stages will be printed to the listing file for every stress
          period in which "HEAD PRINT" is specified in Output Control. If there
          is no Output Control option and PRINT_STAGE is specified, then stages
          are printed for the last time step of each stress period.
    print_flows : boolean
        * print_flows (boolean) keyword to indicate that the list of stream
          reach flow rates will be printed to the listing file for every stress
          period time step in which "BUDGET PRINT" is specified in Output
          Control. If there is no Output Control option and PRINT_FLOWS is
          specified, then flow rates are printed for the last time step of each
          stress period.
    save_flows : boolean
        * save_flows (boolean) keyword to indicate that stream reach flow terms
          will be written to the file specified with "BUDGET FILEOUT" in Output
          Control.
    stage_filerecord : [stagefile]
        * stagefile (string) name of the binary output file to write stage
          information.
    budget_filerecord : [budgetfile]
        * budgetfile (string) name of the binary output file to write budget
          information.
    ts_filerecord : [ts6_filename]
        * ts6_filename (string) defines a time-series file defining time series
          that can be used to assign time-varying values. See the "Time-
          Variable Input" section for instructions on using the time-series
          capability.
    obs_filerecord : [obs6_filename]
        * obs6_filename (string) name of input file to define observations for
          the SFR package. See the "Observation utility" section for
          instructions for preparing observation input files. Table
          reftable:obstype lists observation type(s) supported by the SFR
          package.
    mover : boolean
        * mover (boolean) keyword to indicate that this instance of the SFR
          Package can be used with the Water Mover (MVR) Package. When the
          MOVER option is specified, additional memory is allocated within the
          package to store the available, provided, and received water.
    maximum_iterations : double
        * maximum_iterations (double) value that defines an maximum number of
          Streamflow Routing Newton-Raphson iterations allowed for a reach. By
          default, texttt{maxsfrit} is equal to 100.
    maximum_depth_change : double
        * maximum_depth_change (double) value that defines the depth closure
          tolerance. By default, texttt{dmaxchg} is equal to :math:`1 \\times
          10^{-5}`.
    unit_conversion : double
        * unit_conversion (double) value (or conversion factor) that is used in
          calculating stream depth for stream reach. A constant of 1.486 is
          used for flow units of cubic feet per second, and a constant of 1.0
          is used for units of cubic meters per second. The constant must be
          multiplied by 86,400 when using time units of days in the simulation.
    nreaches : integer
        * nreaches (integer) integer value specifying the number of stream
          reaches. There must be texttt{nreaches} entries in the PACKAGEDATA
          block.
    sfrrecarray : [rno, cellid, rlen, rwid, rgrd, rtp, rbth, rhk, man, ncon,
      ustrf, ndv, aux, boundname]
        * rno (integer) integer value that defines the reach number associated
          with the specified PACKAGEDATA data on the line. texttt{rno} must be
          greater than zero and less than or equal to texttt{nreaches}. Reach
          information must be specified for every reach or the program will
          terminate with an error. The program will also terminate with an
          error if information for a reach is specified more than once.
        * cellid ((integer, ...)) The keyword texttt{`none'} must be specified
          for reaches that are not connected to an underlying GWF cell. The
          keyword texttt{`none'} is used for reaches that are in cells that
          have texttt{IDOMAIN} values less than one or are in areas not covered
          by the GWF model grid. Reach-aquifer flow is not calculated if the
          keyword texttt{`none'} is specified.
        * rlen (double) real value that defines the reach length. texttt{rlen}
          must be greater than zero.
        * rwid (double) real value that defines the reach width. texttt{rwid}
          must be greater than zero.
        * rgrd (double) real value that defines the stream gradient (slope)
          across the reach. texttt{rgrd} must be greater than zero.
        * rtp (double) real value that defines the top elevation of the reach
          streambed.
        * rbth (double) real value that defines the thickness of the reach
          streambed. texttt{rbth} can be any value if texttt{cellid} is
          texttt{`none'}. Otherwise, texttt{rbth} must be greater than zero.
        * rhk (double) real value that defines the hydraulic conductivity of
          the reach streambed. texttt{rhk} can be any positive value if
          texttt{cellid} is texttt{`none'}. Otherwise, texttt{rhk} must be
          greater than zero.
        * man (string) real or character value that defines the Manning's
          roughness coefficient for the reach. texttt{man} must be greater than
          zero. If the Options block includes a texttt{TIMESERIESFILE} entry
          (see the "Time-Variable Input" section), values can be obtained from
          a time series by entering the time-series name in place of a numeric
          value.
        * ncon (integer) integer value that defines the number of reaches
          connected to the reach.
        * ustrf (double) real value that defines the fraction of upstream flow
          from each upstream reach that is applied as upstream inflow to the
          reach. The sum of all texttt{ustrf} values for all reaches connected
          to the same upstream reach must be equal to one and texttt{ustrf}
          must be greater than or equal to zero.
        * ndv (integer) integer value that defines the number of downstream
          diversions for the reach.
        * aux (double) represents the values of the auxiliary variables for
          each stream reach. The values of auxiliary variables must be present
          for each stream reach. The values must be specified in the order of
          the auxiliary variables specified in the OPTIONS block. If the
          package supports time series and the Options block includes a
          TIMESERIESFILE entry (see the "Time-Variable Input" section), values
          can be obtained from a time series by entering the time-series name
          in place of a numeric value.
        * boundname (string) name of the stream reach cell. boundname is an
          ASCII character variable that can contain as many as 40 characters.
          If boundname contains spaces in it, then the entire name must be
          enclosed within single quotes.
    reach_connectivityrecarray : [rno, ic]
        * rno (integer) integer value that defines the reach number associated
          with the specified CONNECTIONDATA data on the line. texttt{rno} must
          be greater than zero and less than or equal to texttt{NREACHES}.
          Reach connection information must be specified for every reach or the
          program will terminate with an error. The program will also terminate
          with an error if connection information for a reach is specified more
          than once.
        * ic (integer) integer value that defines the reach number of the reach
          connected to the current reach and whether it is connected to the
          upstream or downstream end of the reach. Negative texttt{ic} numbers
          indicate connected reaches are connected to the downstream end of the
          current reach. Positive texttt{ic} numbers indicate connected reaches
          are connected to the upstream end of the current reach. The absolute
          value of texttt{ic} must be greater than zero and less than or equal
          to texttt{NREACHES}.
    reach_diversionsrecarray : [rno, idv, iconr, cprior]
        * rno (integer) integer value that defines the reach number associated
          with the specified DIVERSIONS data on the line. texttt{rno} must be
          greater than zero and less than or equal to texttt{NREACHES}. Reach
          diversion information must be specified for every reach with a
          texttt{ndv} value greater than 0 or the program will terminate with
          an error. The program will also terminate with an error if diversion
          information for a given reach diversion is specified more than once.
        * idv (integer) integer value that defines the downstream diversion
          number for the diversion for reach texttt{rno}. texttt{idv} must be
          greater than zero and less than or equal to texttt{ndv} for reach
          texttt{rno}.
        * iconr (integer) integer value that defines the downstream reach that
          will receive the diverted water. texttt{idv} must be greater than
          zero and less than or equal to texttt{NREACHES}. Furthermore, reach
          texttt{iconr} must be a downstream connection for reach texttt{rno}.
        * cprior (string) character string value that defines the the
          prioritization system for the diversion, such as when insufficient
          water is available to meet all diversion stipulations, and is used in
          conjunction with the value of texttt{flow} value specified in the
          texttt{STRESS_PERIOD_DATA} section. Available diversion options
          include: (1) texttt{cprior} = `FRACTION', then the amount of the
          diversion is computed as a fraction of the streamflow leaving reach
          texttt{rno} (:math:`Q_{DS}`); in this case, 0.0 :math:`\\le`
          texttt{divflow} :math:`\\le` 1.0. (2) texttt{cprior} = `EXCESS', a
          diversion is made only if :math:`Q_{DS}` for reach texttt{rno}
          exceeds the value of texttt{divflow}. If this occurs, then the
          quantity of water diverted is the excess flow (:math:`Q_{DS} -`
          texttt{divflow}) and :math:`Q_{DS}` from reach texttt{rno} is set
          equal to texttt{divflow}. This represents a flood-control type of
          diversion, as described by Danskin and Hanson (2002). (3)
          texttt{cprior} = `THRESHOLD', then if :math:`Q_{DS}` in reach
          texttt{rno} is less than the specified diversion flow
          (texttt{divflow}), no water is diverted from reach texttt{rno}. If
          :math:`Q_{DS}` in reach texttt{rno} is greater than or equal to
          (texttt{divflow}), (texttt{divflow}) is diverted and :math:`Q_{DS}`
          is set to the remainder (:math:`Q_{DS} -` texttt{divflow})). This
          approach assumes that once flow in the stream is sufficiently low,
          diversions from the stream cease, and is the `priority' algorithm
          that originally was programmed into the STR1 Package (Prudic, 1989).
          (4) texttt{cprior} = `UPTO' -- if :math:`Q_{DS}` in reach texttt{rno}
          is greater than or equal to the specified diversion flow
          (texttt{divflow}), :math:`Q_{DS}` is reduced by texttt{divflow}. If
          :math:`Q_{DS}` in reach texttt{rno} is less than (texttt{divflow}),
          texttt{divflow} is set to :math:`Q_{DS}` and there will be no flow
          available for reaches connected to downstream end of reach
          \texttt{rno}.
    reachperiodrecarray : [rno, sfrsetting]
        * rno (integer) integer value that defines the reach number associated
          with the specified PERIOD data on the line. texttt{rno} must be
          greater than zero and less than or equal to texttt{NREACHES}.
        * sfrsetting (keystring) line of information that is parsed into a
          keyword and values. Keyword values that can be used to start the
          texttt{sfrsetting} string include: texttt{STATUS}, texttt{MANNING},
          texttt{STAGE}, texttt{INFLOW}, texttt{RAINFALL}, texttt{EVAPORATION},
          texttt{RUNOFF}, texttt{DIVERSION}, texttt{UPSTREAM_FRACTION}, and
          texttt{AUXILIARY}.
            stage : [string]
                * stage (string) real or character value that defines the stage
                  for the reach. The specified texttt{stage} is only applied if
                  the reach uses the simple routing option. If texttt{STAGE} is
                  not specified for reaches that use the simple routing option,
                  the specified stage is set to the top of the reach. If the
                  Options block includes a texttt{TIMESERIESFILE} entry (see
                  the "Time-Variable Input" section), values can be obtained
                  from a time series by entering the time-series name in place
                  of a numeric value.
            diversionrecord : [idv, divrate]
                * idv (integer) diversion number.
                * divrate (double) real or character value that defines the
                  volumetric diversion (texttt{divflow}) rate for the
                  streamflow routing reach. If the Options block includes a
                  TIMESERIESFILE entry (see the "Time-Variable Input" section),
                  values can be obtained from a time series by entering the
                  time-series name in place of a numeric value.
            manning : [string]
                * manning (string) real or character value that defines the
                  Manning's roughness coefficient for the reach.
                  texttt{manning} must be greater than zero. If the Options
                  block includes a texttt{TIMESERIESFILE} entry (see the "Time-
                  Variable Input" section), values can be obtained from a time
                  series by entering the time-series name in place of a numeric
                  value.
            rainfall : [string]
                * rainfall (string) real or character value that defines the
                  volumetric rate per unit area of water added by precipitation
                  directly on the streamflow routing reach. If the Options
                  block includes a TIMESERIESFILE entry (see the "Time-Variable
                  Input" section), values can be obtained from a time series by
                  entering the time-series name in place of a numeric value. By
                  default, rainfall rates are zero for each reach.
            upstream_fraction : [double]
                * upstream_fraction (double) real value that defines the
                  fraction of upstream flow (texttt{ustrf}) from each upstream
                  reach that is applied as upstream inflow to the reach. The
                  sum of all texttt{ustrf} values for all reaches connected to
                  the same upstream reach must be equal to one.
            runoff : [string]
                * runoff (string) real or character value that defines the
                  volumetric rate of diffuse overland runoff that enters the
                  streamflow routing reach. If the Options block includes a
                  TIMESERIESFILE entry (see the "Time-Variable Input" section),
                  values can be obtained from a time series by entering the
                  time-series name in place of a numeric value. By default,
                  runoff rates are zero for each reach.
            status : [string]
                * status (string) keyword option to define stream reach status.
                  texttt{status} can be texttt{ACTIVE}, texttt{INACTIVE}, or
                  texttt{SIMPLE}. The texttt{SIMPLE} texttt{status} option
                  simulates streamflow using a user-specified stage for a reach
                  or a stage set to the top of the reach (depth = 0). In cases
                  where the simulated leakage calculated using the specified
                  stage exceeds the sum of inflows to the reach, the stage is
                  set to the top of the reach and leakage is set equal to the
                  sum of inflows. Upstream factions should be changed using the
                  texttt{UPSTREAM_FRACTION} texttt{sfrsetting} if the status
                  for one or more reaches is changed to texttt{ACTIVE} or
                  texttt{INACTIVE}. For example, if one of two downstream
                  connections for a reach is inactivated, the upstream fraction
                  for the active and inactive downstream reach should be
                  changed to 1.0 and 0.0, respectively, to ensure that the
                  active reach receives all of the downstream outflow from the
                  upstream reach. By default, texttt{status} is texttt{ACTIVE}.
            evaporation : [string]
                * evaporation (string) real or character value that defines the
                  volumetric rate per unit area of water subtracted by
                  evaporation from the streamflow routing reach. A positive
                  evaporation rate should be provided. If the Options block
                  includes a TIMESERIESFILE entry (see the "Time-Variable
                  Input" section), values can be obtained from a time series by
                  entering the time-series name in place of a numeric value. By
                  default, evaporation rates are zero for each reach.
            inflow : [string]
                * inflow (string) real or character value that defines the
                  volumetric inflow rate for the streamflow routing reach. If
                  the Options block includes a TIMESERIESFILE entry (see the
                  "Time-Variable Input" section), values can be obtained from a
                  time series by entering the time-series name in place of a
                  numeric value. By default, inflow rates are zero for each
                  reach.
            auxiliaryrecord : [auxname, auxval]
                * auxname (string) name for the auxiliary variable to be
                  assigned texttt{auxval}. texttt{auxname} must match one of
                  the auxiliary variable names defined in the texttt{OPTIONS}
                  block. If texttt{auxname} does not match one of the auxiliary
                  variable names defined in the texttt{OPTIONS} block the data
                  are ignored.
                * auxval (double) value for the auxiliary variable. If the
                  Options block includes a TIMESERIESFILE entry (see the "Time-
                  Variable Input" section), values can be obtained from a time
                  series by entering the time-series name in place of a numeric
                  value.

    """
    auxiliary = ListTemplateGenerator(('gwf6', 'sfr', 'options', 
                                       'auxiliary'))
    stage_filerecord = ListTemplateGenerator(('gwf6', 'sfr', 'options', 
                                              'stage_filerecord'))
    budget_filerecord = ListTemplateGenerator(('gwf6', 'sfr', 'options', 
                                               'budget_filerecord'))
    ts_filerecord = ListTemplateGenerator(('gwf6', 'sfr', 'options', 
                                           'ts_filerecord'))
    obs_filerecord = ListTemplateGenerator(('gwf6', 'sfr', 'options', 
                                            'obs_filerecord'))
    sfrrecarray = ListTemplateGenerator(('gwf6', 'sfr', 'packagedata', 
                                         'sfrrecarray'))
    reach_connectivityrecarray = ListTemplateGenerator((
        'gwf6', 'sfr', 'connectiondata', 'reach_connectivityrecarray'))
    reach_diversionsrecarray = ListTemplateGenerator((
        'gwf6', 'sfr', 'diversions', 'reach_diversionsrecarray'))
    reachperiodrecarray = ListTemplateGenerator(('gwf6', 'sfr', 'period', 
                                                 'reachperiodrecarray'))
    package_abbr = "gwfsfr"
    package_type = "sfr"
    dfn = [["block options", "name auxiliary", "type string", 
            "shape (naux)", "reader urword", "optional true"],
           ["block options", "name boundnames", "type keyword", "shape", 
            "reader urword", "optional true"],
           ["block options", "name print_input", "type keyword", 
            "reader urword", "optional true"],
           ["block options", "name print_stage", "type keyword", 
            "reader urword", "optional true"],
           ["block options", "name print_flows", "type keyword", 
            "reader urword", "optional true"],
           ["block options", "name save_flows", "type keyword", 
            "reader urword", "optional true"],
           ["block options", "name stage_filerecord", 
            "type record stage fileout stagefile", "shape", "reader urword", 
            "tagged true", "optional true"],
           ["block options", "name stage", "type keyword", "shape", 
            "in_record true", "reader urword", "tagged true", 
            "optional false"],
           ["block options", "name stagefile", "type string", 
            "preserve_case true", "shape", "in_record true", "reader urword", 
            "tagged false", "optional false"],
           ["block options", "name budget_filerecord", 
            "type record budget fileout budgetfile", "shape", "reader urword", 
            "tagged true", "optional true"],
           ["block options", "name budget", "type keyword", "shape", 
            "in_record true", "reader urword", "tagged true", 
            "optional false"],
           ["block options", "name fileout", "type keyword", "shape", 
            "in_record true", "reader urword", "tagged true", 
            "optional false"],
           ["block options", "name budgetfile", "type string", 
            "preserve_case true", "shape", "in_record true", "reader urword", 
            "tagged false", "optional false"],
           ["block options", "name ts_filerecord", 
            "type record ts6 filein ts6_filename", "shape", "reader urword", 
            "tagged true", "optional true"],
           ["block options", "name ts6", "type keyword", "shape", 
            "in_record true", "reader urword", "tagged true", 
            "optional false"],
           ["block options", "name filein", "type keyword", "shape", 
            "in_record true", "reader urword", "tagged true", 
            "optional false"],
           ["block options", "name ts6_filename", "type string", 
            "preserve_case true", "in_record true", "reader urword", 
            "optional false", "tagged false"],
           ["block options", "name obs_filerecord", 
            "type record obs6 filein obs6_filename", "shape", "reader urword", 
            "tagged true", "optional true"],
           ["block options", "name obs6", "type keyword", "shape", 
            "in_record true", "reader urword", "tagged true", 
            "optional false"],
           ["block options", "name obs6_filename", "type string", 
            "preserve_case true", "in_record true", "tagged false", 
            "reader urword", "optional false"],
           ["block options", "name mover", "type keyword", "tagged true", 
            "reader urword", "optional true"],
           ["block options", "name maximum_iterations", 
            "type double precision", "reader urword", "optional true"],
           ["block options", "name maximum_depth_change", 
            "type double precision", "reader urword", "optional true"],
           ["block options", "name unit_conversion", 
            "type double precision", "reader urword", "optional true"],
           ["block dimensions", "name nreaches", "type integer", 
            "reader urword", "optional false"],
           ["block packagedata", "name sfrrecarray", 
            "type recarray rno cellid rlen rwid rgrd rtp rbth rhk man ncon " 
            "ustrf ndv aux boundname", 
            "shape (maxbound)", "reader urword"],
           ["block packagedata", "name rno", "type integer", "shape", 
            "tagged false", "in_record true", "reader urword"],
           ["block packagedata", "name cellid", "type integer", 
            "shape (ncelldim)", "tagged false", "in_record true", 
            "reader urword"],
           ["block packagedata", "name rlen", "type double precision", 
            "shape", "tagged false", "in_record true", "reader urword"],
           ["block packagedata", "name rwid", "type double precision", 
            "shape", "tagged false", "in_record true", "reader urword"],
           ["block packagedata", "name rgrd", "type double precision", 
            "shape", "tagged false", "in_record true", "reader urword"],
           ["block packagedata", "name rtp", "type double precision", 
            "shape", "tagged false", "in_record true", "reader urword"],
           ["block packagedata", "name rbth", "type double precision", 
            "shape", "tagged false", "in_record true", "reader urword"],
           ["block packagedata", "name rhk", "type double precision", 
            "shape", "tagged false", "in_record true", "reader urword"],
           ["block packagedata", "name man", "type string", "shape", 
            "tagged false", "in_record true", "reader urword", 
            "time_series true"],
           ["block packagedata", "name ncon", "type integer", "shape", 
            "tagged false", "in_record true", "reader urword"],
           ["block packagedata", "name ustrf", "type double precision", 
            "shape", "tagged false", "in_record true", "reader urword"],
           ["block packagedata", "name ndv", "type integer", "shape", 
            "tagged false", "in_record true", "reader urword"],
           ["block packagedata", "name aux", "type double precision", 
            "in_record true", "tagged false", "shape (naux)", "reader urword", 
            "time_series true", "optional true"],
           ["block packagedata", "name boundname", "type string", "shape", 
            "tagged false", "in_record true", "reader urword", 
            "optional true"],
           ["block connectiondata", "name reach_connectivityrecarray", 
            "type recarray rno ic", "shape (maxbound)", "reader urword"],
           ["block connectiondata", "name rno", "type integer", "shape", 
            "tagged false", "in_record true", "reader urword"],
           ["block connectiondata", "name ic", "type integer", 
            "shape (ncon(rno))", "tagged false", "in_record true", 
            "reader urword"],
           ["block diversions", "name reach_diversionsrecarray", 
            "type recarray rno idv iconr cprior", "shape (maxbound)", 
            "reader urword"],
           ["block diversions", "name rno", "type integer", "shape", 
            "tagged false", "in_record true", "reader urword"],
           ["block diversions", "name idv", "type integer", "shape", 
            "tagged false", "in_record true", "reader urword"],
           ["block diversions", "name iconr", "type integer", "shape", 
            "tagged false", "in_record true", "reader urword"],
           ["block diversions", "name cprior", "type string", "shape", 
            "tagged false", "in_record true", "reader urword"],
           ["block period", "name iper", "type integer", 
            "block_variable True", "in_record true", "tagged false", "shape", 
            "valid", "reader urword", "optional false"],
           ["block period", "name reachperiodrecarray", 
            "type recarray rno sfrsetting", "shape", "reader urword"],
           ["block period", "name rno", "type integer", "shape", 
            "tagged false", "in_record true", "reader urword"],
           ["block period", "name sfrsetting", 
            "type keystring status manning stage inflow rainfall evaporation " 
            "runoff diversionrecord upstream_fraction auxiliaryrecord", 
            "shape", "tagged false", "in_record true", "reader urword"],
           ["block period", "name status", "type string", "shape", 
            "tagged true", "in_record true", "reader urword"],
           ["block period", "name manning", "type string", "shape", 
            "tagged true", "in_record true", "reader urword", 
            "time_series true"],
           ["block period", "name stage", "type string", "shape", 
            "tagged true", "in_record true", "reader urword", 
            "time_series true"],
           ["block period", "name inflow", "type string", "shape", 
            "tagged true", "in_record true", "reader urword", 
            "time_series true"],
           ["block period", "name rainfall", "type string", "shape", 
            "tagged true", "in_record true", "reader urword", 
            "time_series true"],
           ["block period", "name evaporation", "type string", "shape", 
            "tagged true", "in_record true", "reader urword", 
            "time_series true"],
           ["block period", "name runoff", "type string", "shape", 
            "tagged true", "in_record true", "reader urword", 
            "time_series true"],
           ["block period", "name diversionrecord", 
            "type record diversion idv divrate", "shape", "tagged", 
            "in_record true", "reader urword"],
           ["block period", "name diversion", "type keyword", "shape", 
            "in_record true", "reader urword"],
           ["block period", "name idv", "type integer", "shape", 
            "tagged false", "in_record true", "reader urword"],
           ["block period", "name divrate", "type double precision", 
            "shape", "tagged false", "in_record true", "reader urword", 
            "time_series true"],
           ["block period", "name upstream_fraction", 
            "type double precision", "shape", "tagged true", "in_record true", 
            "reader urword"],
           ["block period", "name auxiliaryrecord", 
            "type record auxiliary auxname auxval", "shape", "tagged", 
            "in_record true", "reader urword"],
           ["block period", "name auxiliary", "type keyword", "shape", 
            "in_record true", "reader urword"],
           ["block period", "name auxname", "type string", "shape", 
            "tagged false", "in_record true", "reader urword"],
           ["block period", "name auxval", "type double precision", "shape", 
            "tagged false", "in_record true", "reader urword", 
            "time_series true"]]

    def __init__(self, model, add_to_package_list=True, auxiliary=None,
                 boundnames=None, print_input=None, print_stage=None,
                 print_flows=None, save_flows=None, stage_filerecord=None,
                 budget_filerecord=None, ts_filerecord=None,
                 obs_filerecord=None, mover=None, maximum_iterations=None,
                 maximum_depth_change=None, unit_conversion=None,
                 nreaches=None, sfrrecarray=None,
                 reach_connectivityrecarray=None,
                 reach_diversionsrecarray=None, reachperiodrecarray=None,
                 fname=None, pname=None, parent_file=None):
        super(ModflowGwfsfr, self).__init__(model, "sfr", fname, pname,
                                            add_to_package_list, parent_file)        

        # set up variables
        self.auxiliary = self.build_mfdata("auxiliary",  auxiliary)
        self.boundnames = self.build_mfdata("boundnames",  boundnames)
        self.print_input = self.build_mfdata("print_input",  print_input)
        self.print_stage = self.build_mfdata("print_stage",  print_stage)
        self.print_flows = self.build_mfdata("print_flows",  print_flows)
        self.save_flows = self.build_mfdata("save_flows",  save_flows)
        self.stage_filerecord = self.build_mfdata("stage_filerecord", 
                                                  stage_filerecord)
        self.budget_filerecord = self.build_mfdata("budget_filerecord", 
                                                   budget_filerecord)
        self.ts_filerecord = self.build_mfdata("ts_filerecord",  ts_filerecord)
        self.obs_filerecord = self.build_mfdata("obs_filerecord", 
                                                obs_filerecord)
        self.mover = self.build_mfdata("mover",  mover)
        self.maximum_iterations = self.build_mfdata("maximum_iterations", 
                                                    maximum_iterations)
        self.maximum_depth_change = self.build_mfdata("maximum_depth_change", 
                                                      maximum_depth_change)
        self.unit_conversion = self.build_mfdata("unit_conversion", 
                                                 unit_conversion)
        self.nreaches = self.build_mfdata("nreaches",  nreaches)
        self.sfrrecarray = self.build_mfdata("sfrrecarray",  sfrrecarray)
        self.reach_connectivityrecarray = self.build_mfdata(
            "reach_connectivityrecarray",  reach_connectivityrecarray)
        self.reach_diversionsrecarray = self.build_mfdata(
            "reach_diversionsrecarray",  reach_diversionsrecarray)
        self.reachperiodrecarray = self.build_mfdata("reachperiodrecarray", 
                                                     reachperiodrecarray)
