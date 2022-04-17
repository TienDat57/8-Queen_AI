from pysat.solvers import Solver
def SatSolver(clauses):
    '''
        clauses: [[], [], [], ...]
    '''
    s = Solver()
    
    for clause in clauses:
        s.add_clause(clause)

    s.solve()

    if s.get_status():
        m = s.get_model()
        return [q for q in m if q > 0]
    
    return []
